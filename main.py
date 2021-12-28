import argparse
import jinja2 as t
import pandas as pd

templates = t.Environment(loader=t.FileSystemLoader(searchpath="./"))


# returns DataFrame(code, en, zh)
def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    # cut useless columns
    data = data.iloc[:, [2, 3, 4]]
    # remove empty rows
    data = data[~data.isnull().any(axis=1)]
    # convert type
    data.iloc[:, 0] = data.iloc[:, 0].astype('int64')
    data.iloc[:, 1] = data.iloc[:, 1].astype('str')
    data.iloc[:, 2] = data.iloc[:, 2].astype('str')
    # trim spaces
    data.iloc[:, 1] = data.iloc[:, 1].apply(lambda x: x.strip())
    data.iloc[:, 2] = data.iloc[:, 2].apply(lambda x: x.strip())
    # normalize column names
    data = data.set_axis(['code', 'en', 'zh'], axis=1)
    return data


def render_template(data: pd.DataFrame, template_path) -> str:
    renderer = templates.get_template(template_path)
    return renderer.render(data=data)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate glue codes from csv files.')
    parser.add_argument('output',
                        metavar='FILEPATH',
                        type=str,
                        help='target output path.')
    parser.add_argument('--template', '-t',
                        type=str,
                        help='path of the template to be used.')
    parser.add_argument('--input', '-i',
                        type=str,
                        help='source data file, in .csv format.')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    result = render_template(read_data(args.input), args.template)
    with open(args.output, 'w+', encoding='utf-8') as f:
        f.write(result)
