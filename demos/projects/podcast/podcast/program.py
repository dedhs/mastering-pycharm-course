import service


def main():
    print_header()
    service.downlaod_info()
    show_titles()


def print_header():
    print("------------------------------------------------")
    print("             PODCAST DOWNLOADER")
    print("------------------------------------------------")


def show_titles():
    start = service.get_min_episode_id()
    end = service.get_max_episode_id()

    for episode_id in range(start, end + 1):
        episode = service.get_details(episode_id)
        print(f'{episode.id}. -> {episode.title}')


if __name__ == '__main__':
    main()
