# Web Responsive Screenshots

A simple utility for Web Developers that takes screenshots of multiple web pages
in multiple resolutions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

* [Google Chrome](https://www.google.com/intl/it_it/chrome/) - It's a cross-platform web browser developed by Google;
* [Python](https://www.python.org/) - It's a programming language that lets you work quickly
and integrate systems more effectively.

Check your `pip` version and upgrade it if necessary:
```
pip --version
```

### Installing

If you have Git installed on your computer you can clone this project with the following command:

```
git clone https://github.com/fgiorgio/web-responsive-screenshots.git
```

or download it manually otherwise.

#### Virtual Env

Project has a built-in python virtual environment with all you need to run the tool.

Install the `virtualenv` package:
```
pip install virtualenv
```

Activate the virtual environment:
```
source venv/bin/activate
```

Deactivate the virtual environment:
```
deactivate
```

#### Local env

You can install and use all the packages locally on your machine, run the following commands:

```
pip install selenium
```

## Configurations

The project uses two files to work correctly.

### Pages file

It's a CSV file containing all the URLs of the pages to take a screenshots.
Each row contains the following ordered values:
* **URL** - the url of the page;
* **File Name** - the prefix of the output image file;
* **Wait Time (seconds)** - by default (wait time = 0 seconds) the screenshot is taken after the page is
fully loaded, but there are cases when it's better to wait few seconds,
for example if there are animations on the page.

Example:
```
http://127.0.0.1/;Home;5
https://www.google.com/;Google;0
https://www.mywebsite.com/;My_Website;3
```

### Configuration file

It's a JSON file containing all the configurations for the process.
Some of the configuration options can be setted directly on the command line.
The following options can be specified:
* **Config File** - The relative position and name of the configuration file (default: config.json);
* **Input File** - The relative position and name of the CSV file containing the pages informations (default: pages.csv);
* **CSV Delimiter** - The delimiter used in the CSV file (default: ";");
* **Output Dir** - The relative position and name of the directory that will contain the project (default: screenshots);
* **Project Name** - The name of the project, used as sub-directory in the output root (default: project);
* **Resolutions** - The list of screen resolutions to take screenshots of.

Example:
```
{
  "project_name": "MyProject",
  "input_file": "pages.csv",
  "csv_delimiter": ";",
  "output_dir": "screenshots",
  "resolutions": [
    "1920x1080",
    "1024x768",
    "800x600",
    "320x480"
  ]
}
```

## Run

* Open the console
* Navigate to the project root
* Run `python wrs.py`

Use the following command to view all the possible arguments:
```
python wrs.py -h
```

## Built With

* [Selenium](https://www.selenium.dev/) - Selenium WebDriver is a collection of language specific bindings to drive a browser.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/fgiorgio/web-responsive-screenshots/tags). 

## Authors

* **Francesco Giorgio** - [giorgio.dev](https://giorgio.dev)

See also the list of [contributors](https://github.com/fgiorgio/web-responsive-screenshots/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details