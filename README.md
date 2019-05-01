# Avatar Maker
Get images from [gravatar](https://www.gravatar.com/)

This project uses [requests](https://github.com/kennethreitz/requests) (which is HTTP library for Python)

## About Input
`input.json` includes request input.  
You can change this file to make your own icon.  
parameters are as follows:

|parameters|options|descriptions|
|---|---|---|
|txt|String|source text. which is used for calculating HASH.|
|d|||
||`404`|do not load any image if none is associated with the email hash, instead return an HTTP 404 (File Not Found) response|
||`mp`|(mystery-person) a simple, cartoon-style silhouetted outline of a person (does not vary by email hash)|
||`identicon`|a geometric pattern based on an email hash|
||`monsterid`|a generated 'monster' with different colors, faces, etc|
||`wavatar`|generated faces with differing features and backgrounds|
||`retro`|awesome generated, 8-bit arcade-style pixelated faces|
||`robohash`|a generated robot with different colors, faces, etc|
||`blank`|a transparent PNG image (border added to HTML below for demonstration purposes)|
|r|||
||`g`|suitable for display on all websites with any audience type.|
||`pg`|may contain rude gestures, provocatively dressed individuals, the lesser swear words, or mild violence.|
||`r`|may contain such things as harsh profanity, intense violence, nudity, or hard drug use.|
||`x`|may contain hardcore sexual imagery or extremely disturbing violence.|
|s|Number|You may request images anywhere from 1px up to 2048px, however note that many users have lower resolution images, so requesting larger sizes may result in pixelation/low-quality images.|

Ref: https://www.gravatar.com/site/implement/images/