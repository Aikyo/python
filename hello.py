import sys
"""
i am a py
"""
print("hello")
def hello():
    print('hello')

a = 10
str = "i am kiko!"

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print ('Usage: python input_name output_name')
        exit(1)
    f_input = sys.argv[1]
    f_output = sys.argv[2]
    hello()
