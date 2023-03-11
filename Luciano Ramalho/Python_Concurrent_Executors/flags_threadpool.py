from concurrent import futures

from flags import get_flag, save_flag, main


def download_one(cc: str):
    image = get_flag(cc)
    save_flag(img=image, filename=f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


def download_many(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list))
    return len(list(res))


if __name__ == '__main__':
    main(downloader=download_many)

