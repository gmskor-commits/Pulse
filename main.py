"""
간단한 Flet 테스트 앱 - APK 빌드 테스트용 v2
"""
import flet as ft


def main(page: ft.Page):
    page.title = "간단한 카운터 앱"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.padding = 20

    # 카운터 상태
    counter = 0

    # 카운터 텍스트
    counter_text = ft.Text(
        value=str(counter),
        size=80,
        weight=ft.FontWeight.BOLD,
        color="#4A7AFF"
    )

    # 카운터 증가 함수
    def increment(e):
        nonlocal counter
        counter += 1
        counter_text.value = str(counter)
        page.update()

    # 카운터 감소 함수
    def decrement(e):
        nonlocal counter
        counter -= 1
        counter_text.value = str(counter)
        page.update()

    # 리셋 함수
    def reset(e):
        nonlocal counter
        counter = 0
        counter_text.value = str(counter)
        page.update()

    # 버튼들
    increment_btn = ft.ElevatedButton(
        "증가 (+)",
        on_click=increment,
        bgcolor="#4A7AFF",
        color="#FFFFFF",
        width=200,
        height=50
    )

    decrement_btn = ft.ElevatedButton(
        "감소 (-)",
        on_click=decrement,
        bgcolor="#FFB74D",
        color="#FFFFFF",
        width=200,
        height=50
    )

    reset_btn = ft.OutlinedButton(
        "리셋",
        on_click=reset,
        width=200,
        height=50
    )

    # 메인 컨텐츠
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text(
                        "🎯 간단한 카운터",
                        size=30,
                        weight=ft.FontWeight.BOLD,
                        color="#E8EDFF"
                    ),
                    padding=20
                ),
                ft.Container(
                    content=counter_text,
                    alignment=ft.alignment.center,
                    padding=30
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            increment_btn,
                            decrement_btn,
                            reset_btn
                        ],
                        spacing=20,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    alignment=ft.alignment.center,
                    padding=20
                ),
                ft.Container(
                    content=ft.Text(
                        "APK 빌드 테스트용 앱",
                        size=14,
                        color="#8C9BCC"
                    ),
                    padding=20
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
