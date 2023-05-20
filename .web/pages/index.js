import { Fragment, useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, isTrue, preventDefault, refs, set_val, updateState, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, Center, Divider, Grid, GridItem, Heading, HStack, Image, Input, Link, Spacer, Text, useColorMode, VStack } from "@chakra-ui/react"
import NextLink from "next/link"
import NextHead from "next/head"

import dynamic from 'next/dynamic'
const Plot = dynamic(() => import('react-plotly.js'), { ssr: false });


const PING = "http://localhost:8000/ping"
const EVENT = "ws://localhost:8000/event"
const UPLOAD = "http://localhost:8000/upload"

export default function Component() {
  const [state, setState] = useState({"all_guesses": ["", "", "", "", ""], "ceo": "", "chart_data": {"columns": ["x", "y"], "data": []}, "chart_data_downloaded": false, "chart_x": [], "chart_y": [], "city": "", "data_downloaded": false, "end_screen": false, "get_daily_ticker": {}, "guessed_ticker": "", "guesses": 0, "industry": "", "inp_guess": "", "is_hydrated": false, "main_chart": [{"customdata": [], "hovertemplate": "%{customdata[0]:.2f} USD", "legendgroup": "", "line": {"color": "#ffba32", "dash": "solid", "width": 3}, "marker": {"symbol": "circle"}, "mode": "lines", "name": "", "orientation": "v", "showlegend": false, "x": [], "xaxis": "x", "y": [], "yaxis": "y", "type": "scatter", "hoverlabel": {"font": {"color": "white", "size": 20}, "bgcolor": "#1a1a1a", "bordercolor": "#ffba32"}}], "mkt_cap": "", "name": "", "rev": "", "ticker": "", "ticker_downloaded": false, "ticker_in_sp100": true, "events": [{"name": "state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "processing": false})
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()

  const Event = (events, _e) => {
      preventDefault(_e);
      setState({
        ...state,
        events: [...state.events, ...events],
      })
  }

  const File = files => setState({
    ...state,
    files,
  })

  useEffect(()=>{
    if(!isReady) {
      return;
    }
    if (!socket.current) {
      connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
    }
    const update = async () => {
      if (result.state != null){
        setState({
          ...result.state,
          events: [...state.events, ...result.events],
        })

        setResult({
          state: null,
          events: [],
          processing: false,
        })
      }

      await updateState(state, setState, result, setResult, router, socket.current)
    }
    update()
  })
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Center sx={{"margin": "10px 0px 0px 0px", "spacing": "0.5em", "width": "100%"}}>
  <VStack spacing="0.5em" sx={{"width": "80%"}}>
  <Box sx={{"width": "100%", "backgroundColor": "#1a1a1a", "borderRadius": "15px", "borderColor": "white", "borderWidth": "thin", "padding": 2.5}}>
  <HStack>
  <Image src="/market.png" sx={{"height": "64px", "width": "64px"}}/>
  <Heading size="3xl" sx={{"backgroundImage": "linear-gradient(45deg, #b53921 0.75%, #ffba32 88.52%)", "backgroundClip": "text"}}>
  {`S t o c k l e`}
</Heading>
  <Spacer/>
  <VStack>
  <Text sx={{"fontSize": 10, "color": "grey"}}>
  {`made by`}
</Text>
  <Text sx={{"fontSize": 10, "color": "grey"}}>
  {`Alan Śliwiński`}
</Text>
</VStack>
  <NextLink href="https://github.com/viseryon/stockle" passHref={true}>
  <Link as="span">
  <Image src="/github.png" sx={{"height": "32px", "width": "32px"}}/>
</Link>
</NextLink>
  <NextLink href="https://twitter.com/SliwinskiAlan" passHref={true}>
  <Link as="span">
  <Image src="/twitter_logo_rounded.png" sx={{"height": "32px", "width": "32px"}}/>
</Link>
</NextLink>
  <NextLink href="https://www.linkedin.com/in/alan-sliwinski/" passHref={true}>
  <Link as="span">
  <Image src="/linkedin.png" sx={{"height": "32px", "width": "38px"}}/>
</Link>
</NextLink>
</HStack>
</Box>
  <HStack spacing="0.5em" sx={{"width": "100%"}}>
  <Box sx={{"backgroundColor": "#1a1a1a", "borderRadius": "15px", "borderColor": "white", "borderWidth": "thin", "padding": 2.5}}>
  <Plot data={state.main_chart} layout={{"font": {"color": "white"}, "legend": {"tracegroupgap": 0}, "margin": {"b": 25, "l": 25, "r": 25, "t": 25}, "paper_bgcolor": "#1a1a1a", "plot_bgcolor": "#1a1a1a", "template": "...", "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "showgrid": false, "title": {"text": ""}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "showgrid": false, "title": {"text": ""}}, "displayModeBar": false, "height": 600, "width": 600}}/>
</Box>
  <VStack spacing="0.5em" sx={{"width": "100%"}}>
  <Box sx={{"width": "100%", "backgroundColor": "#1a1a1a", "borderRadius": "15px", "borderColor": "white", "borderWidth": "thin", "padding": 2.5}}>
  <Center>
  <HStack>
  <Heading size="2xl" sx={{"as": "b", "color": "white"}}>
  {`Guess the  `}
</Heading>
  <Heading size="2xl" sx={{"as": "b", "color": "#ffba32"}}>
  {` T I C K E R`}
</Heading>
</HStack>
</Center>
</Box>
  <Box sx={{"width": "100%", "backgroundColor": "#1a1a1a", "borderRadius": "15px", "borderColor": "white", "borderWidth": "thin", "padding": 2.5}}>
  <VStack>
  <Text sx={{"align": "center", "color": "white"}}>
  {`To make it easier only companies that are in `}
  <NextLink href="https://en.wikipedia.org/wiki/S%26P_100" passHref={true}>
  <Link as="span" sx={{"color": "#ffba32"}}>
  {`S&P 100`}
</Link>
</NextLink>
  {` index are included. The S&P 100 Index is a stock market index of United States stocks maintained by Standard & Poor's.`}
</Text>
  <Text sx={{"color": "white"}}>
  {`Good luck! Have fun!`}
</Text>
</VStack>
</Box>
  <Box sx={{"borderRadius": "15px", "borderColor": "white", "borderWidth": "thin", "padding": 2.5, "width": "100%", "backgroundColor": "#1a1a1a"}}>
  <Grid templateColumns="1fr 4fr 7fr 2fr">
  <Heading size="lg" sx={{"as": "b", "color": "#ffba32"}}>
  {`#`}
</Heading>
  <Heading size="lg" sx={{"as": "b", "color": "#ffba32"}}>
  {`Metric`}
</Heading>
  <Heading size="lg" sx={{"as": "b", "color": "#ffba32"}}>
  {`Value`}
</Heading>
  <Heading size="lg" sx={{"as": "b", "color": "#ffba32"}}>
  {`Guesses`}
</Heading>
  <Divider orientation="horizontal" sx={{"borderColor": "white"}} variant="solid"/>
  <Divider orientation="horizontal" sx={{"borderColor": "white"}} variant="solid"/>
  <Divider orientation="horizontal" sx={{"borderColor": "white"}} variant="solid"/>
  <Divider orientation="horizontal" sx={{"borderColor": "white"}} variant="solid"/>
  <Text sx={{"color": "white"}}>
  {`1`}
</Text>
  <Text sx={{"color": "white"}}>
  {`Revenue TTM`}
</Text>
  <Text sx={{"color": "white"}}>
  {state.rev}
</Text>
  <GridItem>
  <Text sx={{"textAlign": "center", "color": "white"}}>
  {state.all_guesses.at(0)}
</Text>
</GridItem>
  <Text sx={{"color": "white"}}>
  {`2`}
</Text>
  <Text sx={{"color": "white"}}>
  {`City`}
</Text>
  <Text sx={{"color": "white"}}>
  {state.city}
</Text>
  <GridItem>
  <Text sx={{"textAlign": "center", "color": "white"}}>
  {state.all_guesses.at(1)}
</Text>
</GridItem>
  <Text sx={{"color": "white"}}>
  {`3`}
</Text>
  <Text sx={{"color": "white"}}>
  {`Industry`}
</Text>
  <Text sx={{"color": "white"}}>
  {state.industry}
</Text>
  <GridItem>
  <Text sx={{"textAlign": "center", "color": "white"}}>
  {state.all_guesses.at(2)}
</Text>
</GridItem>
  <Text sx={{"color": "white"}}>
  {`4`}
</Text>
  <Text sx={{"color": "white"}}>
  {`Market Cap`}
</Text>
  <Text sx={{"color": "white"}}>
  {state.mkt_cap}
</Text>
  <GridItem>
  <Text sx={{"textAlign": "center", "color": "white"}}>
  {state.all_guesses.at(3)}
</Text>
</GridItem>
  <Text sx={{"color": "white"}}>
  {`5`}
</Text>
  <Text sx={{"color": "white"}}>
  {`CEO`}
</Text>
  <Text sx={{"color": "white"}}>
  {state.ceo}
</Text>
  <GridItem>
  <Text sx={{"textAlign": "center", "color": "white"}}>
  {state.all_guesses.at(4)}
</Text>
</GridItem>
</Grid>
</Box>
  <HStack sx={{"width": "100%"}}>
  <Input isDisabled={state.end_screen} onBlur={_e => Event([E("state.set_inp_guess", {guess:_e.target.value})], _e)} placeholder="example: AAPL" sx={{"color": "white", "borderRadius": "15px", "backgroundColor": "#1a1a1a"}} type="text"/>
  <Button isDisabled={state.end_screen} onClick={_e => Event([E("state.make_inp_guess", {})], _e)} sx={{"bg": "white", "borderRadius": "15px", "_hover": {"bg": "#ffba32", "boxShadow": "0px 0px 15px 5px #ffba32"}}}>
  {`Guess`}
</Button>
</HStack>
  <Box sx={{"width": "100%", "backgroundColor": "#1a1a1a", "borderRadius": "15px", "borderColor": "white", "borderWidth": "thin", "padding": 2.5}}>
  <Center>
  <Fragment>
  {isTrue(state.end_screen) ? (
  <Fragment>
  <HStack>
  <Heading size="2xl" sx={{"as": "b", "color": "white"}}>
  {`The ticker was... `}
</Heading>
  <Heading size="2xl" sx={{"as": "b", "color": "#ffba32"}}>
  {state.ticker}
</Heading>
</HStack>
</Fragment>
) : (
  <Fragment>
  {isTrue(state.ticker_in_sp100) ? (
  <Fragment>
  {isTrue(state.guessed_ticker) ? (
  <Fragment>
  <HStack>
  <Heading size="2xl" sx={{"as": "b", "color": "white"}}>
  {`It's not `}
</Heading>
  <Heading size="2xl" sx={{"as": "b", "color": "#ffba32"}}>
  {state.guessed_ticker}
</Heading>
</HStack>
</Fragment>
) : (
  <Fragment>
  <HStack>
  <Heading size="2xl" sx={{"as": "b", "color": "white", "_hover": {"color": "#ffba32"}}}>
  {`LET'S PLAY!`}
</Heading>
</HStack>
</Fragment>
)}
</Fragment>
) : (
  <Fragment>
  <HStack>
  <Heading size="2xl" sx={{"as": "b", "color": "#ffba32"}}>
  {state.guessed_ticker}
</Heading>
  <Heading size="2xl" sx={{"as": "b", "color": "white"}}>
  {`is not in S&P100`}
</Heading>
</HStack>
</Fragment>
)}
</Fragment>
)}
</Fragment>
</Center>
</Box>
</VStack>
</HStack>
  <Spacer/>
</VStack>
  <NextHead>
  <title>
  {`Stockle`}
</title>
  <meta content="A wordle-type game about stocks!" name="description"/>
  <meta content="market_icon.ico" property="og:image"/>
</NextHead>
</Center>
  )
}
