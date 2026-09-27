# Selenium Framework (Beginner Level) — Unittest + PyTest + POM

Same capstone requirements as before — Login and Product Search on
[automationexercise.com](https://automationexercise.com) — but written
using only what a typical intro Selenium course covers before it
introduces `unittest`/`pytest` properly:

- Plain classes with `__init__(self, driver)` — no base-class abstraction
- Browser choice via `if/elif` on a string (`config.py`), same pattern as `majortest.py`
- `time.sleep()` after actions instead of `WebDriverWait`
- `try/except` to check "does this element exist" instead of custom wait helpers
- CSV read with plain `csv.DictReader`, no wrapper class
- No config-parsing library — just two variables at the top of `config.py`

## Structure

```
selenium_framework_basic/
├── config.py                  # BROWSER + BASE_URL + get_driver()
├── pages/
│   ├── home_page.py            # go_to_login_page(), go_to_products_page(), is_logged_in(), logout()
│   ├── login_page.py           # login(), get_error_message()
│   └── search_page.py          # search_product(), get_result_count()
├── testdata/
│   ├── login_data.csv
│   └── search_data.csv
├── tests/
│   ├── test_login_unittest.py  # unittest.TestCase, setUp/tearDown, subTest loop
│   ├── test_login_pytest.py    # plain pytest functions + parametrize
│   └── test_search_pytest.py
├── conftest.py                 # one fixture (open/close browser) + screenshot-on-fail
├── pytest.ini
├── screenshots/                # saved automatically on failure
├── reports/                    # pytest_html report goes here
└── requirements.txt
```

## Why this still counts as "Unittest + PyTest + POM"

- **POM**: `HomePage`, `LoginPage`, `SearchPage` each hold their own
  locators and actions — the tests never write a `By.XPATH` themselves.
  That's the whole point of POM; it doesn't require fancy base classes.
- **Unittest**: `test_login_unittest.py` is a real `unittest.TestCase`
  with `setUp`, `tearDown`, and `subTest` for looping over CSV rows.
- **PyTest**: `test_login_pytest.py` / `test_search_pytest.py` use a
  `driver` fixture and `@pytest.mark.parametrize` — the standard PyTest
  way to loop over data, just without extra plugins beyond `pytest-html`.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Before running

Open `testdata/login_data.csv` and replace the `valid_login` row's
email/password with a real account you registered on
automationexercise.com (via its Signup page) — the site has no shared
demo login.

## Running

```bash
python -m unittest tests.test_login_unittest -v      # unittest suite
pytest                                                # runs everything in tests/
```

`pytest` produces `reports/report.html`. Any failed test also drops a
screenshot into `screenshots/`.

## If you want to go further later

Once your course covers `WebDriverWait`, you'd replace the `time.sleep()`
calls in the page classes with:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "search_product")))
```
Everything else — the folder layout, the POM classes, the CSV data — stays the same.
