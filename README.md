# Python.org Event Scraper

A simple Python web-scraping project built with **Selenium WebDriver**.
The script opens the official Python website, extracts event-related information such as **event time and event name**, stores the results in a dictionary, and prints them to the console.

## 📌 Project Overview

This project demonstrates basic browser automation and web scraping using Selenium.

The script:

1. Launches Google Chrome using Selenium.
2. Opens [Python.org](https://python.org).
3. Keeps the Chrome browser open after the Selenium script finishes.
4. Finds `<time>` elements from the page.
5. Extracts event times.
6. Finds event links from the events section.
7. Extracts event names.
8. Combines the event names and times into a dictionary.
9. Prints the collected event data.
10. Closes the browser.

## 🛠️ Technologies Used

* **Python 3**
* **Selenium**
* **Google Chrome**
* **ChromeDriver**

## 📂 Project Structure

```text
Python-Event-Scraper/
│
├── main.py
├── dependencies.py
└── README.md
```

> `main.py` contains the Selenium scraping logic.
> `dependencies.py` can be used for project-specific dependencies or configuration.

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.x installed
* Google Chrome installed
* Selenium installed
* A compatible ChromeDriver/Selenium Manager setup

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Python-Event-Scraper
```

### 2. Install Selenium

```bash
pip install selenium
```

### 3. Run the script

```bash
python main.py
```

## 🔍 How It Works

The script first creates a Chrome browser configuration:

```python
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
```

The `detach` option keeps the Chrome window open after the WebDriver process ends.

The WebDriver is then initialized:

```python
driver = webdriver.Chrome(options=chrome_option)
```

The Python website is opened with:

```python
driver.get("https://python.org")
```

### Extracting Event Times

The script searches for all `<time>` elements:

```python
time_tag = driver.find_elements(By.TAG_NAME, value="time")
```

The text from each element is collected into a list:

```python
l1 = []

for i in time_tag:
    l1.append(i.text)
```

### Extracting Event Names

The script locates the events section and searches for anchor (`<a>`) elements:

```python
l3 = events_div[0].find_elements(By.TAG_NAME, value="a")
```

The text of each link is then stored:

```python
links = []

for i in l3:
    links.append(i.text)
```

### Creating the Event Dictionary

The extracted times and names are combined into key-value pairs:

```python
pair = {
    'time': f"{l1[j]}",
    'name': f"{links[j]}"
}
```

The final data is stored in a dictionary:

```python
dict.update({i: pair})
```

## 📊 Example Output

The output will have a structure similar to:

```text
{
    0: {
        'time': '2026-10-15',
        'name': 'Example Python Event'
    },
    1: {
        'time': '2026-10-16',
        'name': 'Another Python Event'
    }
}
```

The exact event names and dates will depend on the current content of Python.org.

## 🎯 Learning Objectives

This project was created to practice:

* Selenium WebDriver
* Browser automation
* Finding HTML elements
* `By.TAG_NAME`
* `By.CLASS_NAME`
* XPath selectors
* Extracting `.text`
* Working with lists
* Working with dictionaries
* Combining scraped data
* Basic web scraping concepts

## 🚀 Possible Improvements

The current implementation can be extended in several ways:

* Use more reliable CSS selectors instead of absolute XPath.
* Extract event URLs in addition to names.
* Store the results in JSON or CSV.
* Create a reusable scraping function.
* Add exception handling.
* Handle cases where events are unavailable.
* Remove unnecessary `f-string` usage.
* Replace the dictionary with a list of dictionaries.
* Add logging.
* Schedule the scraper to run automatically.
* Build a Flask API around the scraped event data.

## ⚠️ Notes

This project is intended for **learning Selenium and web automation**.

Websites can change their HTML structure over time. If Python.org changes its page structure, the XPath or element selectors used by the script may need to be updated.

## 👨‍💻 Author

**Om Gaikwad**

A Python/Selenium learning project focused on understanding browser automation and web scraping.

## 📄 License

This project is intended for educational purposes.
