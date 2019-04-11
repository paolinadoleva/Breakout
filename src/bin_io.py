import os
import struct
#from src import Ball, Paddle, Brick
from src.breakout_driver import Ball
from src.breakout_driver import Paddle
from src.breakout_driver import Brick



def read_file(file):
    # Instantiate list (i.e. Memory object)
    int_list = []
    float_list = []

    # Open the file to read in binary
    with open(os.path.join("..//data", file), "rb") as bin_in:
        # Read the file as raw binary
        ba = bytearray(bin_in.read())

    format = ">iidiiiii"
    chunk_size = struct.calcsize(format)
    chunk = ba[0: chunk_size]
    ballx, bally, paddlex, score, lives, level, numbricks = struct.unpack(format, chunk)
    #balltheta, paddlex, score, lives, level, numbricks = struct.unpack(format, chunk)

    ball = Ball(balltheta)

    paddle = Paddle()

    # X, Y, Health
    brick_format = ">iii"

    brick_chunk_size = struct.calcsize(brick_format)

    bricks = []

    for i in range(numbricks - 1):
        start = chunk_size + (i * brick_chunk_size)
        end = start + brick_chunk_size
        chunk = ba[start: end]
        x, y, health = struct.unpack(brick_format, chunk)
        brick = Brick(x, y, health)
        bricks.append(brick)

    return ball, paddle, bricks, score, lives, level


def save_file(file, ball, paddle, bricks, score, lives, level):
    # Designate format
    format = ">iiiiii"
    chunk = struct.pack(format, ball.x, ball.y, score, lives, level, len(bricks))

    # Instantiate an empty bytearray
    ba = bytearray()
    ba.extend(chunk)

    brick_format = ">iii"
    # iterate through each list
    # for brick in bricks:
    #     # Pack each set of bytes
    #     chunk = struct.pack(brick_format, brick.x, brick.y, brick.health)
    #     # Append the bytes to the output
    #     ba.extend(chunk)

    # Open the file to write binary and write the bytes.
    file_path = os.path.join("..//data", file)
    with open(file_path, "wb") as bin_out:
        bin_out.write(ba)
