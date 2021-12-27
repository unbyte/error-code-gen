import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate glue codes from csv files.')
    parser.add_argument('file',
                        metavar='FILEPATH',
                        type=str,
                        help='target output path.')
    parser.add_argument('--language', '-l',
                        type=str,
                        default='typescript',
                        help='output language. Default to typescript.')
    parser.add_argument('--data', '-d',
                        type=str,
                        default='./codes.csv',
                        help='source data file, in .csv format. Default to ./codes.csv')

    return parser.parse_args()


if __name__ == '__main__':
    import reader
    import generator

    args = parse_args()
    data = reader.read_data(args.data)
    result = ''
    if args.language != 'typescript':
        print('not supported yet')
        exit(1)
    else:
        result = generator.render_typescript(data)

    with open(args.file, 'w+', encoding='utf-8') as f:
        f.write(result)
