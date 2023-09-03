import asyncio
import aiofiles
import aiofiles.os

FILE_NAME = "text-file.txt"


async def write_lines_to_file():
    async with aiofiles.open(FILE_NAME, "w") as f:
        for i in range(1, 11):
            await f.write(f"line_{i}\n")


async def read_lines_from_file():
    async with aiofiles.open(FILE_NAME, "r") as f:
        async for line in f:
            print(repr(line))


async def show_write_to_temp_file():
    async with aiofiles.tempfile.NamedTemporaryFile("w+") as f:
        await f.writelines([
            "foo\n",
            "bar\n",
            "spam\n",
            "eggs\n",
        ])
        await f.seek(0)
        async for line in f:
            print(repr(line))

        print(f.name)


async def remove_file():
    await aiofiles.os.remove(FILE_NAME)


async def main():
    await write_lines_to_file()
    await read_lines_from_file()
    await show_write_to_temp_file()
    await remove_file()


if __name__ == "__main__":
    asyncio.run(main())
