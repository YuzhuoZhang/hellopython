def get_play_list(file_list=[]):
    # play_list = []
    # video = ''
    # for file_name in file_list:
    #     for _ in range(len(file_name)):
    #         if file_name[_].isdigit():
    #             video += file_name[_]
    #     play_list.append(video)
    #     video = ''
    # return sorted(play_list)
    return sorted(file_list)


print(get_play_list(
    ['东京喰种3-4',
     '东京喰种3-2',
     '东京喰种3-7',
     '东京喰种3-1',
     '东京喰种3-6',
     '东京喰种3-3',
     '东京喰种3-5'
     ]))
