import paddle
import paddle.fluid as fluid
import paddle.dataset.mnist as reader
from paddleslim.quant import quant_post_dynamic

paddle.enable_static()
quant_post_dynamic(
        model_dir='output/ssd_mobilenet_v1_voc',
        save_model_dir='output/ssd_mobilenet_v1_voc',
        model_filename='output/ssd_mobilenet_v1_voc/__model__',
        params_filename='output/ssd_mobilenet_v1_voc/__params__',
        save_model_filename='output/ssd_mobilenet_v1_voc/__model__',
        save_params_filename='output/ssd_mobilenet_v1_voc/__params__')
