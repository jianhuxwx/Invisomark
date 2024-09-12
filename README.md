##IMPORTANT!!!!
Due to personal reasons, the Invisomark project will be Archived soon.

# INVISOMARK: Invisible Watermarking Tool

![LOGO](https://github.com/jianhuxwx/invisomark/assets/114718101/2c8f4a9b-628d-4ac3-883e-c0882a091758)

## Introduction

Welcome to INVISOMARK, an innovative open-source software designed for seamless and transparent watermarking. Our tool embodies the principles of openness, freedom, and non-intrusiveness, ensuring your images retain their original aesthetic while being discreetly protected.

## Features

- **Invisible Watermarking**: INVISOMARK utilizes advanced techniques to embed watermarks that are completely transparent, ensuring no visible alteration to your images. But at the same time still protect your image.
- **Antagonistic Blind Watermark**: Most blind watermarks are easy to be damaged. Antagonistic Blind Watermark does not need to be worried about any artificial damage. For specific proofing, see below.
- **Image Trace**: Tracing back to the source of the image. Search for the vulnerable users that use your image without their permission.
- **Line Watermark**: By extracting the sketch of the picture and providing additional watermarks through the sketch line. Your image will be protected without any visible watermark but still traceable.
- **Digital Signature**: Create a Digital Signature based on the hash number of the picture and verify it easily.
- **Open Source**: Embracing the open-source community, our software's code is freely available for use, modification, and distribution.
- **User-Friendly Interface**: Designed with simplicity in mind, our tool allows for easy watermarking of images without the need for technical expertise.
- **High Compatibility**: Compatible with a wide range of image formats, ensuring versatility in its application.
- **Security and Protection**: Offers an additional layer of security for your digital images, ideal for photographers, artists, and content creators.

## Antagonistic Blind Watermark

| Damage | Image Example | Watermark Extract |
| --- | --- | --- |
| Rotate 45 Degrees | <img width="457" alt="截屏2023-12-15 下午7 55 31" src="https://github.com/jianhuxwx/invisomark/assets/114718101/c26ddce8-f649-4a3b-84fb-e0c539bbff2a"> | Keyfox |
| Random crop |  <img width="163" alt="截屏2023-12-15 下午7 54 34" src="https://github.com/jianhuxwx/invisomark/assets/114718101/f866fdd6-bde3-450d-84f4-633330610256"> | Keyfox |
| Masks |  <img width="268" alt="截屏2023-12-15 下午7 57 03" src="https://github.com/jianhuxwx/invisomark/assets/114718101/9fc646ba-1d01-40ae-a36b-e7e126da896f"> | Keyfox |
| Vertical cut |  <img width="130" alt="截屏2023-12-15 下午7 57 32" src="https://github.com/jianhuxwx/invisomark/assets/114718101/3de8c92d-5dfe-4908-be23-b03fc7b8d79a"> | Keyfox |
| Horizontal cut | <img width="270" alt="截屏2023-12-15 下午7 57 55" src="https://github.com/jianhuxwx/invisomark/assets/114718101/823b1416-7eaa-4016-a3ca-a28f8bf645a1"> | Keyfox |
| Resize |  <img width="283" alt="截屏2023-12-15 下午7 58 27" src="https://github.com/jianhuxwx/invisomark/assets/114718101/03a063c0-0e49-4b8e-8a0f-e977cac3f102"> | Keyfox |
| Pepper Noise | <img width="279" alt="截屏2023-12-15 下午7 59 34" src="https://github.com/jianhuxwx/invisomark/assets/114718101/9cca9fe4-69df-4c23-bbf7-9cb0d04d50f6"> | Keyfox |
| Brightness 10% Down |   <img width="278" alt="截屏2023-12-15 下午8 00 15" src="https://github.com/jianhuxwx/invisomark/assets/114718101/3db6495c-1ff7-4c8d-b18a-3f2e092e7142"> | Keyfox |

## Specific Function

| Watermark | Before Watermark | After Watermark |
| --- | --- | --- |
| Blind Watermark | ![vulpinium_1](https://github.com/jianhuxwx/invisomark/assets/114718101/6146eaa3-b36b-494e-8711-536b45fddc1e)    |  ![vulpinium_1_watermarked](https://github.com/jianhuxwx/invisomark/assets/114718101/a0a7c78c-47f0-48eb-9d67-ae9ff141797d)   |
| Line Watermark |  ![vulpinium_1](https://github.com/jianhuxwx/invisomark/assets/114718101/6146eaa3-b36b-494e-8711-536b45fddc1e)  | ![vulpinium_1_watermarked_lined](https://github.com/jianhuxwx/invisomark/assets/114718101/98beee7a-779e-4329-8d80-9db98d6586c9) |
| Full-Screen Watermark |  ![vulpinium_1](https://github.com/jianhuxwx/invisomark/assets/114718101/6146eaa3-b36b-494e-8711-536b45fddc1e)      | ![vulpinium_1_watermarked_fullscreen](https://github.com/jianhuxwx/invisomark/assets/114718101/e6924ee8-d576-440d-a3ec-038b0d6168fa) |
| Basic Watermark |  ![vulpinium_1](https://github.com/jianhuxwx/invisomark/assets/114718101/6146eaa3-b36b-494e-8711-536b45fddc1e)      |   ![vulpinium_1_watermarked](https://github.com/jianhuxwx/invisomark/assets/114718101/02edd402-0b48-430c-85c8-fb53ebf62bcf) |
| Blur Image |  ![vulpinium_1](https://github.com/jianhuxwx/invisomark/assets/114718101/6146eaa3-b36b-494e-8711-536b45fddc1e)      |   ![vulpinium_1_watermarked_blur](https://github.com/jianhuxwx/invisomark/assets/114718101/d09c19be-5bef-4ccb-8d1c-1323d1a740e7) |

## Usage

Using INVISOMARK is straightforward:

1. Launch the application.
2. Upload the image you wish to watermark.
3. Choose your watermark settings.
4. Apply the watermark.
5. Save the watermarked image.

## Contributing

We welcome contributions from the community! If you're interested in improving INVISOMARK, feel free to fork the repository, make changes, and submit a pull request.

## License

INVISOMARK is released under GNU, which allows for free use, modification, and distribution of the software.

## Special Thanks

Thanks for [guofei9987](https://github.com/guofei9987/blind_watermark/commits?author=guofei9987) to opensource the project **[blind_watermark](https://github.com/guofei9987/blind_watermark)** . The Blind Watermark is based on this project.
