def test_load():
    from LockHub.global_api.loadconfig import load_config
    x = load_config()
    print(x)


if __name__ == "__main__":
    test_load()