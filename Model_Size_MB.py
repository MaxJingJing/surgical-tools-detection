# import torch
#
#
# def getModelSize(model):
#     param_size = 0
#     param_sum = 0
#     for param in model.parameters():
#         param_size += param.nelement() * param.element_size()
#         param_sum += param.nelement()
#     buffer_size = 0
#     buffer_sum = 0
#     for buffer in model.buffers():
#         buffer_size += buffer.nelement() * buffer.element_size()
#         buffer_sum += buffer.nelement()
#     all_size = (param_size + buffer_size) / 1024 / 1024
#     print('模型总大小为：{:.3f}MB'.format(all_size))
#     return (param_size, param_sum, buffer_size, buffer_sum, all_size)
#
#
# import torchvision.models as models
#
# if __name__=='__main__':
#     model_5n = 'exp-5n/weights/best.pt'
#     print(model_5n)
#     model =torch.load(model_5n)
#     param_size, param_sum, buffer_size, buffer_sum, all_size =getModelSize(model_5n)
#     print('model-5n Size\nparam_size{}\n'
#           'param_sum{}\n'
#           'buffer_size{} buffer_sum{}\n all_size{}'.format(param_size, param_sum, buffer_size, buffer_sum, all_size))
#
#
#
#
#     # ----------------------------------------------------------------
#     param_size, param_sum, buffer_size, buffer_sum, all_size = getModelSize(model)
#     print('model-5n Size\nparam_size{}\n'
#           'param_sum{}\n'
#           'buffer_size{} buffer_sum{}\n all_size{}'.format(param_size, param_sum, buffer_size, buffer_sum, all_size))
#     with open("modelSize_log.txt",'w') as f:
#         f.write('param_size=={}'.format(param_size))
#         f.write('param_sum=={}'.format(param_sum))
#         f.write('buffer_size=={}'.format(buffer_size))
#         f.write('buffer_sum=={}'.format(buffer_sum))
#         f.write('all_size=={}'.format(all_size))
#     # ----------------------------------------------------------------
import torch


def getModelSize(model):
    param_size = 0
    param_sum = 0
    for param in model.parameters():
        param_size += param.nelement() * param.element_size()
        param_sum += param.nelement()
    buffer_size = 0
    buffer_sum = 0
    for buffer in model.buffers():
        buffer_size += buffer.nelement() * buffer.element_size()
        buffer_sum += buffer.nelement()
    all_size = (param_size + buffer_size) / 1024 / 1024
    print('模型总大小为：{:.2f}MB'.format(all_size))
    # param_size, param_sum, buffer_size, buffer_sum, all_size = getModelSize(model)
    print('param_size=={}\n'
          'param_sum=={}\n'
          'buffer_size={} buffer_sum={}\n all_size={}'.format(param_size, param_sum, buffer_size, buffer_sum, all_size))
    with open("modelSize_log.txt",'w') as f:
        f.write('param_size={}\n'.format(param_size))#param_size是所有parameters的参数字节MB大小
        f.write('param_sum={}\n'.format(param_sum))
        f.write('buffer_size={}\n'.format(buffer_size))
        f.write('buffer_sum={}\n'.format(buffer_sum))
        f.write('all_size={}\n'.format(all_size))
    return '********ok*******'


if __name__=='__main__':
    model_5n = 'exp-5n/weights/best.pt'
    print(model_5n)
    model =torch.load(model_5n)
    print(model.parameters)
    # getModelSize()