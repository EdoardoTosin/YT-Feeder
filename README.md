# YT-Feeder

## Summary

Simple python script that extracts channel/playlist name and publish date-time.

## Instructions

### Linux
- `git clone https://github.com/EdoardoTosin/YT-Feeder.git`
- `cd YT-Feeder/src && python3 -m pip install -r requirements.txt`
- Example: `python3 main.py UCX6OQ3DkcsbYNE6H8uQQuVA PLoSWVnSA9vG-6geT_u92P9ttBfRLVFhLH`

### Windows
- `git clone https://github.com/EdoardoTosin/YT-Feeder.git`
- `cd YT-Feeder\src; python -m pip install -r requirements.txt`
- Example: `python main.py UCX6OQ3DkcsbYNE6H8uQQuVA PLoSWVnSA9vG-6geT_u92P9ttBfRLVFhLH`

_IMPORTANT: Arguments must be 24 (channel\_id) or 34 (playlist\_id) characters long._

## YouTube Feed XML
- [MrBeast](https://www.youtube.com/channel/UCX6OQ3DkcsbYNE6H8uQQuVA):
    - [Channel Feed](https://www.youtube.com/feeds/videos.xml?channel_id=UCX6OQ3DkcsbYNE6H8uQQuVA)
    - [Playlist Feed](https://www.youtube.com/feeds/videos.xml?playlist_id=PLoSWVnSA9vG-6geT_u92P9ttBfRLVFhLH)
- [jawed](https://www.youtube.com/channel/UC4QobU6STFB0P71PMvOGN5A):
    - [Channel Feed](https://www.youtube.com/feeds/videos.xml?channel_id=UC4QobU6STFB0P71PMvOGN5A)
    - [Playlist Feed](https://www.youtube.com/feeds/videos.xml?playlist_id=PLuhl9TnQPDCnWIhy_KSbtFwXVQnNvgfSh)

## License
This software is released under the terms of the GNU General Public License v3.0. See the [LICENSE](https://github.com/EdoardoTosin/YT-Feeder/tree/main/LICENSE) file for further information.
