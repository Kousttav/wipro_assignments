# Automation Testing Training Documentation

# Milestone 1
# Selenium WebDriver Automation Using Python

---

## Introduction

Selenium is an open-source automation testing framework used to automate web applications across different browsers. Python is widely used with Selenium because of its simplicity, readability, and extensive library support.

This milestone focuses on learning Selenium WebDriver fundamentals, web element interactions, synchronization techniques, handling browser components, framework design, and test automation best practices.

---

## Objectives

- Understand Selenium WebDriver architecture.
- Learn various locator strategies.
- Automate browser interactions.
- Handle alerts, frames, windows, and tables.
- Implement synchronization using Explicit Waits.
- Design automation frameworks using Page Object Model (POM).
- Perform Data Driven Testing (DDT).
- Integrate Selenium with PyTest.

---

## Tools and Technologies

| Tool | Purpose |
|--------|----------|
| Python | Programming Language |
| Selenium WebDriver | Browser Automation |
| Chrome Browser | Test Execution |
| ChromeDriver | Browser Driver |
| PyTest | Testing Framework |
| Pandas | Data Driven Testing |
| PyCharm / VS Code | IDE |

---

# Assignment 1: Multi Locator Challenge

## Objective

Learn different locator strategies available in Selenium.

## Concepts Covered

- ID Locator
- Name Locator
- XPath Locator

## Implementation

- Open SauceDemo website.
- Locate username using ID.
- Locate password using Name.
- Locate login button using XPath.
- Perform login operation.
- Validate successful login by checking URL.

## Outcome

Successfully automated login workflow using multiple locator strategies.

---

# Assignment 2: Synchronization and Explicit Waits

## Objective

Handle dynamic content loading using Selenium waits.

## Concepts Covered

- Explicit Wait
- WebDriverWait
- Expected Conditions

## Implementation

- Open dynamic content page.
- Trigger delayed content loading.
- Wait for content visibility.
- Extract and validate displayed text.

## Outcome

Successfully synchronized automation execution without using time.sleep().

---

# Assignment 3: Dynamic Dropdowns and Checkboxes

## Objective

Automate dynamic UI elements.

## Concepts Covered

- Checkboxes
- Auto-Suggestion Dropdowns
- Iterative Element Selection

## Implementation

- Select multiple checkboxes.
- Verify checkbox state.
- Enter text in auto-suggestion field.
- Iterate through suggestions.
- Select matching option.

## Outcome

Successfully automated dynamic dropdown selection and checkbox validation.

---

# Assignment 4: JavaScript Alerts and Confirmations

## Objective

Handle browser alert popups.

## Concepts Covered

- Alert Box
- Confirm Box
- Prompt Box

## Implementation

- Accept Alert.
- Dismiss Confirm.
- Enter text in Prompt.
- Validate responses.

## Outcome

Successfully automated browser alert interactions.

---

# Assignment 5: HTML Web Table Extraction

## Objective

Extract information from web tables.

## Concepts Covered

- Table Rows
- Table Columns
- Dynamic Data Extraction

## Implementation

- Locate table.
- Iterate through rows and columns.
- Search for matching record.
- Retrieve associated information.

## Outcome

Successfully extracted data from dynamic HTML tables.

---

# Assignment 6: Windows, Tabs and Iframes

## Objective

Handle multiple browser contexts.

## Concepts Covered

- Iframes
- Window Handles
- Multiple Browser Tabs

## Implementation

- Switch to iframe.
- Interact with embedded elements.
- Open new browser window.
- Capture title information.
- Return to parent window.

## Outcome

Successfully switched between frames and windows.

---

# Assignment 7: Page Object Model (POM)

## Objective

Design a maintainable automation framework.

## Framework Structure

```text
Project
│
├── pages
├── tests
└── driver_setup.py
```

## Benefits

- Code Reusability
- Maintainability
- Scalability

## Outcome

Successfully implemented Page Object Model architecture.

---

# Assignment 8: Data Driven Testing (DDT)

## Objective

Execute automation using external datasets.

## Technologies Used

- CSV
- Pandas

## Implementation

- Read credentials from external source.
- Execute multiple test scenarios.
- Validate expected results.

## Outcome

Reduced script duplication and improved test coverage.

---

# Assignment 9: PyTest Integration

## Objective

Integrate Selenium framework with PyTest.

## Concepts Covered

- Fixtures
- Setup and Teardown
- HTML Reports

## Outcome

Successfully generated automated execution reports.

---

## Skills Acquired

- Selenium WebDriver
- Web Element Locators
- Explicit Waits
- Alerts Handling
- Web Tables
- Frames and Windows
- Page Object Model
- Data Driven Testing
- PyTest Framework


