from rich import print
from rich.console import Console
from rich.table import Table

# 기본 텍스트 출력
print("[bold magenta]Hello, Rich![/bold magenta] :sparkles:")

# 콘솔 객체 생성
console = Console()

# 표 만들기
table = Table(title="프로그래밍 언어 인기 순위")

table.add_column("이름", justify="right", style="cyan", no_wrap=True)
table.add_column("나이", style="magenta")
table.add_column("종", justify="right", style="green")

table.add_row("아름", "22", "인간")
table.add_row("사랑이", "13", "가나디")
table.add_row("행운이", "8", "고먐미")

console.print(table)

from rich.progress import Progress
import time

# Progress 객체를 사용하여 진행 바 출력
with Progress() as progress:
    task = progress.add_task("사랭이 식사하는 중...", total=100)

    while not progress.finished:
        progress.update(task, advance=1)  # 진행도 1씩 증가
        time.sleep(0.03)  # 0.03초마다 업데이트 (다운로드 시뮬레이션)

# Progress 객체를 사용하여 진행 바 출력
with Progress() as progress:
    task = progress.add_task("So...so...so 프리징~", total=100)

    while not progress.finished:
        progress.update(task, advance=1)  # 진행도 1씩 증가
        time.sleep(0.03)  # 0.03초마다 업데이트 (다운로드 시뮬레이션)

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.emoji import Emoji

console = Console()

# 귀여운 인사말 출력
greeting = Text("오늘도 파이팅용구리! 🐥💖", style="bold magenta")
console.print(Panel(greeting, title="🌸 오늘의 메시지 🌸", subtitle="운이 볼주머니", style="bright_magenta"))

# 할 일 목록
todos = """
[bold green]✔[/bold green] 사랭이 산책하기 🐶  
[bold yellow]➤[/bold yellow] 책자 완성, 대본쓰기 📚  
[bold blue]☕[/bold blue] 오렌지 주스 마시기 🍊 
"""
console.print(Panel(todos, title="🌼 오늘의 할 일", style="bright_blue"))

# 긍정 메시지
positive = Text("배고프다! 🌈", style="bold cyan")
console.print(Panel(positive, title="🌟 Positive Vibes 🌟", style="cyan"))
