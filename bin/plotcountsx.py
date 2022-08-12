import argparse
import pandas as pd




def get_df(infile):
    df = pd.read_csv(infile, header=None,names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,method='max')
    df['inverse_rank'] = 1 / df['rank']

    return df

def plot_wordcount(df, outfile):
    scatplot = df.plot.scatter(x='word_frequency',
                           y='inverse_rank',
                           figsize=[12, 6],
                           grid=True)
    fig = scatplot.get_figure()
    fig.savefig(outfile)


def main(args):
    df = get_df(args.infile)
    plot_wordcount(df, args.outfile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default='-', help='Input file path')
    parser.add_argument('-o','--outfile', type=str,  help='Output file path')#
    args = parser.parse_args()
    main(args)

