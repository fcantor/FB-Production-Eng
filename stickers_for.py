#!/bin/python3


def stickers_for(phrase):
    ''' This function counts how many "instagram" stickers is needed to build the give phrase '''
    insta_dict = {'i': 1, 'n': 1, 's': 1,
                  't': 1, 'a': 2, 'g': 1, 'r': 1, 'm': 1}
    matching_letters = {}
    count = 0
    # create dictionary with matching letters and letter count
    for i in phrase:
        if i in 'instagram':
            matching_letters[i] = phrase.count(i)
    # count how many stickers needed per
    for key in insta_dict:
        temp = (matching_letters.get(key, 0) %
                insta_dict[key]) + matching_letters.get(key, 0) // insta_dict[key]
        count = max(count, temp)
    return count


if __name__ == "__main__":
    print(stickers_for('artisan martians'))
    print(stickers_for('taming giant gnats'))
    print(stickers_for('stain ram'))
    print(stickers_for('tiara'))
