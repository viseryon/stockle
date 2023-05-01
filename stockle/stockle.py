from pcconfig import config

import pynecone as pc
from stockle import helpers
from datetime import datetime as dt
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random
import asyncio
docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class Confetti(pc.Component):
    """Confetti component."""

    library = "react-confetti"
    tag = "ReactConfetti"


confetti = Confetti.create

class State(pc.State):

    ticker: str
    name: str
    rev: str
    city: str
    industry: str
    mkt_cap: str
    ceo: str

    chart_x: list
    chart_y: list

    data_downloaded: bool = False
    ticker_downloaded: bool = False
    chart_data_downloaded: bool = False

    inp_guess: str
    guessed_ticker: str
    ticker_in_sp100: bool = True
    all_guesses: list = ['' for i in range(5)]
    guesses: int = 0

    end_screen: bool = False
    show_confetti: bool = False

    def make_inp_guess(self):

        print('BEFORE', 'guesses #', self.guesses)
        print('BEFORE', 'game end', self.end_screen)

        if self.guesses == 5 or self.end_screen:
            self.end_screen = True
            return

        self.guessed_ticker = self.inp_guess

        if self.guessed_ticker not in helpers.all_tickers():
            self.ticker_in_sp100 = False
            return
        else:
            self.ticker_in_sp100 = True

        self.all_guesses[self.guesses] = self.guessed_ticker
        self.guesses += 1

        if self.guessed_ticker == self.ticker:
            self.end_screen = True
            print('GAME OVER', 'YOU WIN')
            return self.start_confetti

        if self.guesses == 5:
            print('GAME OVER', 'YOU LOSE')
            self.end_screen = True
            return

    def start_confetti(self):
        """Start the confetti."""
        self.show_confetti = True
        return self.stop_confetti

    async def stop_confetti(self):
        """Stop the confetti."""
        await asyncio.sleep(5)
        self.show_confetti = False



    def set_inp_guess(self, guess):
        self.inp_guess = guess.upper()
        print('self.inp_guess:', self.inp_guess)

    @pc.var
    def chart_data(self) -> pd.DataFrame:
        return pd.DataFrame({'x': self.chart_x, 'y': self.chart_y})

    @pc.var
    def main_chart(self) -> go.Figure:
        fig = px.line(
            self.chart_data,
            x='x',
            y='y',
            custom_data=[self.chart_y],
        )

        fig.update_traces(
            hovertemplate='%{customdata[0]:.2f} USD',

            hoverlabel=dict(
                bgcolor='#1a1a1a',
                bordercolor='#ffba32',
                font=dict(
                    color='white',
                    size=20
                )
            ),
            line_color='#ffba32', line_width=3
        )

        fig.update_xaxes(title='')
        fig.update_yaxes(title='')
        fig.update_layout(
            margin=dict(t=5, l=5, r=5, b=5),
            paper_bgcolor="#1a1a1a",
            plot_bgcolor="#1a1a1a",
            font=dict(color='white'),
            xaxis_showgrid=False, yaxis_showgrid=False,
        )

        return fig


class TodayTicker(pc.Model, table=True):

    ticker: str
    name: str
    rev: str
    city: str
    industry: str
    mkt_cap: str
    ceo: str

    today_date: str


class TodayChart(pc.Model, table=True):

    dates: str
    price: float
    ticker: str

    today_date: str


class GetDailyTicker(State):

    def get_ticker(self):

        if self.data_downloaded:
            return

        today_date = dt.today().strftime(r'%Y-%m-%d')

        with pc.session() as session:
            today_ticker = session.query(TodayTicker).filter(
                TodayTicker.today_date.contains(today_date)).all()

            if today_ticker:
                ticker_of_the_day = today_ticker[0].dict()

                self.ticker = ticker_of_the_day['ticker']
                self.name = helpers.sp100_tickers[self.ticker]['Name']

                self.rev = ticker_of_the_day['rev']
                self.city = ticker_of_the_day['city']
                self.industry = ticker_of_the_day['industry']
                self.mkt_cap = ticker_of_the_day['mkt_cap']
                self.ceo = ticker_of_the_day['ceo']

                self.ticker_downloaded = True

            else:
                all_tickers = helpers.all_tickers()
                new_ticker = random.choice(list(all_tickers))

                x, y, rev, city, industry, mkt_cap, ceo = helpers.data_call(
                    new_ticker)

                session.add(
                    TodayTicker(
                        ticker=new_ticker, name=all_tickers[new_ticker][
                            'Name'], rev=rev, city=city, industry=industry, mkt_cap=mkt_cap, ceo=ceo,
                        today_date=today_date
                    )
                )

                session.commit()

        with pc.session() as session:

            today_chart = session.query(TodayChart).filter(
                TodayChart.today_date.contains(today_date)).all()

            if today_chart:
                chart_of_the_day = today_chart

                c_x, c_y = [], []
                for chart in chart_of_the_day:
                    c_x.append(chart.dict()['dates'])
                    c_y.append(chart.dict()['price'])

                self.chart_x = c_x
                self.chart_y = c_y

                self.chart_data_downloaded = True

            else:

                for dates, price in zip(x, y):
                    session.add(
                        TodayChart(dates=dates, price=price,
                                   ticker=new_ticker, today_date=today_date)
                    )

                session.commit()

        if self.chart_data_downloaded and self.ticker_downloaded:
            self.data_downloaded = True

        return GetDailyTicker.get_ticker


def navbar() -> pc.component:
    return pc.box(
        pc.hstack(
            pc.image(src="/market.png", height='64px', width='64px'),
            pc.heading('S t o c k l e',
                       background_image="linear-gradient(45deg, #b53921 0.75%, #ffba32 88.52%)",
                       background_clip='text',
                       size="3xl"),
            pc.spacer(),
            pc.vstack(
                pc.text('made by', font_size=10, color='grey'),
                pc.text('Alan Śliwiński', font_size=10, color='grey'),
            ),
            pc.link(
                pc.image(src="/github.png",
                         height='32px', width='32px'),
                href=helpers.GITHUB_URL,
            ),
            pc.link(
                pc.image(src="/twitter_logo_rounded.png",
                         height='32px', width='32px'),
                href=helpers.TWITTER_URL,
            ),
            pc.link(
                pc.image(src="/linkedin.png",
                         height='32px', width='38px'),
                href=helpers.LINKEDIN_URL,
            ),
        ),
        width="100%",
    )


def chart_area() -> pc.component:
    return pc.box(
        pc.plotly(
            data=State.main_chart, layout=helpers.CHART_LAYOUT,
        ),
    )


def hints_title() -> pc.component:
    return pc.box(
        pc.center(
            pc.hstack(
                pc.heading('Guess the  ', as_='b', color='white', size='2xl'),
                pc.heading(' T I C K E R', as_='b',
                           size='2xl', color='#ffba32'),
            )
        ),
        width='100%'
    )


def hints_desc() -> pc.component:
    return pc.box(
        pc.vstack(
            pc.text(
                'To make it easier only companies that are in ',
                pc.link('S&P 100', href='https://en.wikipedia.org/wiki/S%26P_100',
                        color='#ffba32'
                        ),
                "index are included. The S&P 100 Index is a stock market index of United States stocks maintained by Standard & Poor's.",
                align='center'
            ),
            pc.text('Good luck! Have fun!'),
        ),
        width='100%'
    )


def hints_area() -> pc.component:
    return pc.box(
        pc.grid(

            pc.heading('#', as_='b',
                       color='#ffba32', size='lg'),
            pc.heading('Metric', as_='b',
                       color='#ffba32', size='lg'),
            pc.heading('Value', as_='b',
                       color='#ffba32', size='lg'),
            pc.heading('Guesses', as_='b',
                       color='#ffba32', size='lg'),

            pc.divider(orientation='horizontal',
                       border_color='white', variant='solid'),
            pc.divider(orientation='horizontal',
                       border_color='white', variant='solid'),
            pc.divider(orientation='horizontal',
                       border_color='white', variant='solid'),
            pc.divider(orientation='horizontal',
                       border_color='white', variant='solid'),

            pc.text('1'),
            pc.text('Revenue TTM'),
            pc.text(State.rev),
            pc.grid_item(pc.text(State.all_guesses[0], text_align='center')),

            pc.text('2'),
            pc.text('City'),
            pc.text(State.city),
            pc.grid_item(pc.text(State.all_guesses[1], text_align='center')),

            pc.text('3'),
            pc.text('Industry'),
            pc.text(State.industry),
            pc.grid_item(pc.text(State.all_guesses[2], text_align='center')),

            pc.text('4'),
            pc.text('Market Cap'),
            pc.text(State.mkt_cap),
            pc.grid_item(pc.text(State.all_guesses[3], text_align='center')),

            pc.text('5'),
            pc.text('CEO'),
            pc.text(State.ceo),
            pc.grid_item(pc.text(State.all_guesses[4], text_align='center')),

            template_columns='1fr 4fr 7fr 2fr',
        ),
        border_radius="15px",
        border_color="white",
        border_width="thin",
        padding=2.5,
        width='100%',
    )


def guesses() -> pc.component:
    return pc.hstack(
        pc.input(
            placeholder='example: AAPL',
            color='white',
            on_blur=State.set_inp_guess,
            border_radius="15px",
            is_disabled=State.end_screen,
            background_color='#1a1a1a',
        ),
        pc.button(
            'Guess',
            bg='white',
            on_click=State.make_inp_guess,
            border_radius="15px",
            is_disabled=State.end_screen,
            _hover={'bg': '#ffba32', 'boxShadow': '0px 0px 15px 5px #ffba32'},
        ),
        width='100%'
    )


def answer() -> pc.component:

    return pc.box(
        pc.center(
            pc.cond(
                State.end_screen,
                pc.hstack(
                    pc.heading('The ticker was... ', as_='b',
                               color='white', size='2xl'),
                    pc.heading(State.ticker, as_='b',
                               color='#ffba32', size='2xl'),
                ),
                pc.cond(
                    State.ticker_in_sp100,
                    pc.cond(
                        State.guessed_ticker,
                        pc.hstack(
                            pc.heading("It's not ", as_='b',
                                       color='white', size='2xl'),
                            pc.heading(State.guessed_ticker, as_='b',
                                       color='#ffba32', size='2xl'),
                        ),
                        pc.hstack(
                            pc.heading("LET'S PLAY!", as_='b',
                                       color='white', size='2xl',
                                       _hover={'color': '#ffba32'}),
                        ),
                    ),
                    pc.hstack(
                        pc.heading(State.guessed_ticker, as_='b',
                                   color='#ffba32', size='2xl'),
                        pc.heading("is not in S&P100", as_='b',
                                   color='white', size='2xl')
                    )
                )
            )
        ),
        width='100%',
    )


def main_page():
    return pc.center(
        pc.cond(
            State.show_confetti,
            confetti(),
        ),
        pc.vstack(
            navbar(),
            pc.hstack(
                chart_area(),
                pc.vstack(
                    hints_title(),
                    hints_desc(),
                    hints_area(),
                    guesses(),
                    answer(),
                    spacing='0.5em',
                    width='100%',
                ),
                spacing='0.5em',
                width="100%",
            ),
            pc.spacer(),
            spacing='0.5em',
            width='80%',
        ),
        margin='10px 0px 0px 0px',
        spacing='0.5em',
        width='100%',
    )


style = {
    'background_color': '#1a1a1a',
    'font_color': 'white',
    'font_size': 20,
    pc.Text: {
        'color': 'white'
    },
    pc.Box: {
        'background_color': '#1a1a1a',
        'border_radius': "15px",
        'border_color': "white",
        'border_width': "thin",
        'padding': 2.5,
    }
}


app = pc.App(state=State, style=style)
app.add_page(main_page,
             route='/',
             on_load=GetDailyTicker.get_ticker,
             title='Stockle',
             image='market_icon.ico',
             description='A wordle-type game about stocks!'
             )
app.compile()
