TARGET = test
PADDLE_LITE_DIR=/opt/plite

CFLAGS = -O3 -Wall -std=c++11 `pkg-config --cflags opencv`
CFLAGS += -march=armv7-a -mfloat-abi=hard -mfpu=neon -I$(PADDLE_LITE_DIR)/include

LDFLAGS = -O3 -Wall -std=c++11 `pkg-config --libs opencv`
LDFLAGS += -L$(PADDLE_LITE_DIR)/lib

CC = g++

all: $(TARGET)

$(TARGET): $(TARGET).o
	$(CC) $(LDFLAGS) -o $@ $^ `pkg-config --libs opencv` -lpthread -lpaddle_full_api_shared

%.o: %.cpp
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $(TARGET) *.a *.o *~

