from selenium import webdriver
import os
import sys
import getopt
import csv
import json
import time


configs = {}
defaults = {
    'project_name': 'project',
    'input_file': 'pages.csv',
    'config_file': 'config.json',
    'csv_delimiter': ';',
    'output_dir': 'screenshots'
}


def display_help():
    print('USAGE:')
    print('    -h Display help')
    print('    -n <project_name> (default: '+defaults['project_name']+')')
    print('    -i <input_file> (default: '+defaults['input_file']+')')
    print('    -d <csv_delimiter> (default: '+defaults['csv_delimiter']+')')
    print('    -o <output_dir> (default: '+defaults['output_dir']+')')
    print('    -c <config_file> (default: '+defaults['config_file']+')')


def handle_args():
    global configs
    try:
        argv = sys.argv[1:]
        opts, args = getopt.getopt(argv, "hn:d:i:d:o:c:")
        for opt, arg in opts:
            if opt == '-h':
                display_help()
                sys.exit()
            elif opt == "-n":
                configs['project_name'] = arg
            elif opt == "-i":
                configs['input_file'] = arg
            elif opt == "-d":
                configs['csv_delimiter'] = arg
            elif opt == "-o":
                configs['output_dir'] = arg
            elif opt == "-c":
                configs['config_file'] = arg
    except getopt.GetoptError:
        display_help()
        sys.exit(2)
    except Exception as e:
        print('Error handling arguments\n'+str(e))
        sys.exit()


def build_configs():
    global configs, defaults
    try:
        if 'config_file' not in configs.keys():
            configs['config_file'] = defaults['config_file']
        if not os.path.exists(configs['config_file']):
            raise Exception('Configuration file not found ('+configs['config_file']+')')
        with open(configs['config_file'], 'r') as json_handle:
            json_configs = json.load(json_handle)
        for key in json_configs.keys():
            if key not in configs.keys():
                configs[key] = json_configs[key]
        for key in defaults.keys():
            if key not in configs.keys():
                configs[key] = defaults[key]
        if not os.path.exists(configs['input_file']):
            raise Exception('Input file not found ('+configs['input_file']+')')
        if not os.path.exists(configs['output_dir']):
            raise Exception('Output directory not found ('+configs['output_dir']+')')
        if len(configs['resolutions']) == 0:
            raise Exception('No resolutions specified in the config file ('+configs['config_file']+')')
        configs['project_folder'] = os.path.join(configs['output_dir'], configs['project_name'])
        if not os.path.exists(configs['project_folder']):
            os.mkdir(configs['project_folder'])
    except Exception as e:
        print('Error loading configurations\n'+str(e))
        sys.exit()


def load_csv():
    try:
        with open(configs['input_file'], newline='') as csv_handle:
            pages_list = list(csv.reader(csv_handle, delimiter=configs['csv_delimiter']))
        if len(pages_list) == 0:
            raise Exception('No pages specified in the input file ('+configs['input_file']+')')
        for page in pages_list:
            if len(page) != 3:
                raise Exception('Input file not valid (' + configs['input_file'] + ')')
        return pages_list
    except Exception as e:
        print('Error handling csv input file\n'+str(e))
        sys.exit()


def save_screenshot(driver, page, resolution):
    global configs
    url = page[0]
    file_name = page[1]
    wait_time = int(page[2])
    width, height = resolution.split('x')
    driver.set_window_size(width, height)
    driver.get(url)
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width, height)
    if wait_time > 0:
        time.sleep(wait_time)
    el = driver.find_element_by_tag_name('body')
    el.screenshot(configs['project_folder'] + '/' + file_name + '_' + resolution + '.png')


def main():
    global configs
    try:
        handle_args()
        build_configs()
        pages_list = load_csv()
        images_number = len(pages_list)*len(configs['resolutions'])

        browser_options = webdriver.ChromeOptions()
        browser_options.add_argument("headless")
        with webdriver.Chrome("drivers/chromedriver", options=browser_options) as driver:
            count = 1
            for page in pages_list:
                for resolution in configs['resolutions']:
                    save_screenshot(driver, page, resolution)
                    print('Saved '+str(count)+' of '+str(images_number), end="\r")
                    count += 1
        print('Saved '+str(images_number)+' screenshots')

    except Exception as e:
        print(e)
        sys.exit()


if __name__ == "__main__":
    main()
