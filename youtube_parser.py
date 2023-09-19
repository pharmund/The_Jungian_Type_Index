import re
from youtube_transcript_api import YouTubeTranscriptApi
def youtube_parser(url):
    regExp = re.compile(r'^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*')
    match = regExp.match(url)
    print(match.group(7) if match and len(match.group(7)) == 11 else False)
    return match.group(7) if match and len(match.group(7)) == 11 else False

def get_text(link):
    transcript_list = YouTubeTranscriptApi.list_transcripts(link)
    transcript = transcript_list.find_transcript(['en'])
    translated_transcript = transcript.translate('ru')


    file = translated_transcript.fetch()
    result = ''

    for transcript in file:
        result += (transcript['text'])
        result += ' '

    return result

print(get_text('sNeHToxGAJo'))
