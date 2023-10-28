***This branch is unmaintained!***
https://github.com/toriato/stable-diffusion-webui-wd14-tagger/issues/108
---
https://github.com/picobyte/stable-diffusion-webui-wd14-tagger



# Fixed Error on 2023/10/28
I fix all 3 errors on import modules errors.

```
File "E:\stable-diffusion-webui\extensions\stable-diffusion-webui-wd14-tagger\scripts\tagger.py", line 18, in <module>
        from modules.shared import models_path
    ImportError: cannot import name 'models_path' from partially initialized module 'modules.shared' (most likely due to a circular import)
```
```
File "E:\stable-diffusion-webui\extensions\stable-diffusion-webui-wd14-tagger\scripts\tagger.py", line 10, in <module>
        from webui import wrap_gradio_gpu_call
    ImportError: cannot import name 'wrap_gradio_gpu_call' from 'webui'
```
```
File "E:\stable-diffusion-webui\extensions\stable-diffusion-webui-wd14-tagger\scripts\tagger.py", line 45, in refresh_interrogators
shared.cmd_opts.deepdanbooru_projects_path,
AttributeError: 'Namespace' object has no attribute 'deepdanbooru_projects_path'
```

It works on my webui v1.6.0 env


# Tagger for [Automatic1111's WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
Interrogate booru style tags for single or multiple image files using various models, such as DeepDanbooru.

[한국어를 사용하시나요? 여기에 한국어 설명서가 있습니다!](README.ko.md)

## Disclaimer
I didn't make any models, and most of the code was heavily borrowed from the [DeepDanbooru](https://github.com/KichangKim/DeepDanbooru) and MrSmillingWolf's tagger.

## Installation
1. *Extensions* -> *Install from URL* -> Enter URL of this repository -> Press *Install* button
   - or clone this repository under `extensions/`
      ```sh
      $ git clone https://github.com/toriato/stable-diffusion-webui-wd14-tagger.git extensions/tagger
      ```

1. *(optional)* Add interrogate model
   - #### [*Waifu Diffusion 1.4 Tagger by MrSmilingWolf*](docs/what-is-wd14-tagger.md)
      Downloads automatically from the [HuggingFace repository](https://huggingface.co/SmilingWolf/wd-v1-4-vit-tagger) the first time you run it.

   - #### *DeepDanbooru*
      1. Various model files can be found below.
         - [DeepDanbooru models](https://github.com/KichangKim/DeepDanbooru/releases)
         - [e621 model by 🐾Zack🐾#1984](https://discord.gg/BDFpq9Yb7K)
            *(link contains NSFW contents!)*

      1. Move the project folder containing the model and config to `models/deepdanbooru`

      1. The file structure should look like:
         ```
         models/
         └╴deepdanbooru/
           ├╴deepdanbooru-v3-20211112-sgd-e28/
           │ ├╴project.json
           │ └╴...
           │
           ├╴deepdanbooru-v4-20200814-sgd-e30/
           │ ├╴project.json
           │ └╴...
           │
           ├╴e621-v3-20221117-sgd-e32/
           │ ├╴project.json
           │ └╴...
           │
           ...
         ```

1. Start or restart the WebUI.
   - or you can press refresh button after *Interrogator* dropdown box.
   - "You must close stable diffusion completely after installation and re-run it!"


## Model comparison
[Model comparison](docs/model-comparison.md)

## Screenshot
![Screenshot](docs/screenshot.png)

Artwork made by [hecattaart](https://vk.com/hecattaart?w=wall-89063929_3767)

## Copyright

Public domain, except borrowed parts (e.g. `dbimutils.py`)
