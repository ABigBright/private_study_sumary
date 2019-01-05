LOCAL_PATH:= $(call my-dir)

include $(CLEAR_VARS)

LOCAL_SHARED_LIBRARIES := \
	libcutils \
	libbinder \
	libutils \
	libhardware

LOCAL_SRC_FILES:= client.cpp

LOCAL_MODULE_TAGS = eng tests

LOCAL_MODULE:= testClient

include $(BUILD_EXECUTABLE)


include $(CLEAR_VARS)

LOCAL_SHARED_LIBRARIES := \
	libcutils \
	libbinder \
	libutils \
	libhardware

LOCAL_SRC_FILES:=service.cpp
LOCAL_MODULE:= testServer
LOCAL_MODULE_TAGS = eng tests

include $(BUILD_EXECUTABLE)
