# 引用Paddlelite预测库
from paddlelite.lite import *

# 1. 创建opt实例
opt = Opt()
# 2. 指定输入模型地址
opt.set_model_file(r"output/ssd_mobilenet_v1_voc/quantized_model/__model__")
opt.set_param_file(r"output/ssd_mobilenet_v1_voc/quantized_model/__params__")
# opt.set_model_dir(r"output/ssd_mobilenet_v1_voc")
# 3. 指定转化类型： arm、x86、opencl、npu
opt.set_valid_places("intel_fpga,arm")
# 4. 指定模型转化类型： naive_buffer、protobuf
opt.set_model_type("naive_buffer")
# 4. 输出模型地址
opt.set_optimize_out("ssd_opt_slim")
# opt.set_valid_targets("x86")
# 5. 执行模型优化
opt.run()
