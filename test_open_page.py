from playwright.sync_api import Page, expect

def test_open_enter_your_details_form(page: Page):
    page.goto(
        "https://data.fundraiseup.com/qa-test-7R58U3/",
        wait_until="commit",
        timeout=60000
    )

    # 1. Открываем виджет
    expect(page.get_by_text("Click me")).to_be_visible(timeout=60000)
    page.get_by_text("Click me").click()

    # 2. Нажимаем Give Now
    donate_frame = page.frame_locator('iframe[title="Donate Button"]')
    give_now_button = donate_frame.get_by_role("button", name="Give Now")
    expect(give_now_button).to_be_visible(timeout=60000)
    give_now_button.click()

    # 3. Открывается checkout
    checkout_frame = page.frame_locator("iframe#__checkout2")
    expect(
        checkout_frame.get_by_text("Secure donation", exact=False)
    ).to_be_visible(timeout=60000)

    # 4. Выбираем Monthly
    monthly_option = checkout_frame.locator('input[value="monthly"]')
    expect(monthly_option).to_be_visible(timeout=60000)
    monthly_option.check()
    expect(monthly_option).to_be_checked(timeout=60000)

    # 5. Меняем сумму на 5000
    amount_input = checkout_frame.locator('input[type="text"]').first
    expect(amount_input).to_be_visible(timeout=60000)

    amount_input.click()
    amount_input.fill("5000")

    # 6. Нажимаем Donate Monthly
    donate_button = checkout_frame.get_by_role("button", name="Donate", exact=False)
    expect(donate_button).to_be_visible(timeout=60000)
    expect(donate_button).to_be_enabled(timeout=60000)
    donate_button.click()

    # 7. Проверяем Enter your details
    expect(
        checkout_frame.get_by_text("Enter your details", exact=False)
    ).to_be_visible(timeout=60000)

    page.wait_for_timeout(5000)