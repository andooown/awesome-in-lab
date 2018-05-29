# -*- coding: utf-8 -*-

import gensim


def calc_vector(model, positive=None, negative=None):
    similars = model.most_similar(positive, negative)
    for i, v in enumerate(similars):
        print('{0}: {1}, {2}'.format(i + 1, v[0], v[1]))


def main():
    model = gensim.models.Word2Vec.load('model/ja.bin')

    print("カレー + ラーメン = ")
    calc_vector(model, positive=['カレー', 'ラーメン'])
    print()

    print("茶 + 西洋 = ")
    calc_vector(model, positive=['茶', '西洋'])
    print()

    print("スノーボード - 雪 = ")
    calc_vector(model, positive=['スノーボード'], negative=['雪'])
    print()

    print("王 - 男 + 女 = ")
    calc_vector(model, positive=['王', '女'], negative=['男'])
    print()

    print("兄 - 男 + 女 = ")
    calc_vector(model, positive=['兄', '女'], negative=['男'])
    print()


if __name__ == '__main__':
    main()
