---


# Milestone 2
# Behavior Driven Development (BDD) Using Behave Framework

---

## Introduction

Behavior Driven Development (BDD) is a software development methodology that promotes collaboration among developers, testers, and business stakeholders.

Behave is a Python-based BDD framework that uses Gherkin syntax to describe application behavior.

---

## Objectives

- Understand BDD concepts.
- Learn Gherkin syntax.
- Automate scenarios using Behave.
- Integrate Selenium with Behave.
- Implement Page Object Model within BDD.

---

## Tools and Technologies

| Tool | Purpose |
|--------|----------|
| Python | Programming Language |
| Behave | BDD Framework |
| Selenium | Browser Automation |
| Gherkin | Scenario Definition |
| ChromeDriver | Browser Driver |

---

# Assignment 1: Selenium Python and Behave BDD

## Objective

Create end-to-end automation using Behave.

## Components

- Feature Files
- Step Definitions
- Environment Hooks

## Example

```gherkin
Feature: Login Functionality

Scenario: Successful Login

Given User launches SauceDemo website
When User enters username
And User enters password
Then User should login successfully
```

## Outcome

Successfully executed login workflow using BDD methodology.

---

# Assignment 2: Data Driven Automation Using Behave

## Objective

Execute multiple datasets using Scenario Outline.

## Concepts Covered

- Scenario Outline
- Examples Table
- Parameterized Testing

## Benefits

- Reusability
- Reduced Script Duplication
- Improved Coverage

## Outcome

Successfully executed multiple login test combinations.

---

# Assignment 3: Selenium POM with Behave

## Objective

Integrate Page Object Model with Behave framework.

## Framework Structure

```text
features
│
├── login.feature
├── steps
│
pages
│
├── login_page.py
└── inventory_page.py
```

## Benefits

- Cleaner Code Structure
- Reusable Methods
- Easy Maintenance

## Outcome

Successfully implemented a scalable BDD automation framework.

---

## Skills Acquired

- Behavior Driven Development
- Behave Framework
- Gherkin Language
- Scenario Outline
- Environment Hooks
- Page Object Model Integration
