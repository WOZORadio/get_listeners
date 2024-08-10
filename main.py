import requests

# Example for TuneIn API
api_url = "https://api.tunein.com/stations/listeners"
api_key = "your_api_key_here"
station_id = "your_station_id_here"

def get_listeners(target_station):
    '''get a real-time list of listeners of this station'''
    response = requests.get(f"{api_url}?id={station_id}&key={api_key}")

    if response.status_code == 200:
        listener_data = response.json()
        print(listener_data)
    else:
        print(f"Error: {response.status_code}")


# https://support.radiojar.com/support/solutions/articles/5000004606-implementing-the-air-tunein-broadcaster-api
# To integrate this API with your radio station, you will first need to get permission from TuneIn by
# sending them an email at broadcaster-support@tunein.com.
# You need to send them your TuneIn station URL and mention the broadcasting software you're using.
# A sample email text you can use is the following:
#
# "I'd like to ask your permission to use the AIR API for my radio station. My TuneIn station URL is: [replace with your station's TuneIn URL]. I'm using Radiojar to broadcast."
#
# If TuneIn accepts your request, they will reply with a partner ID, a partner Key and a station ID.
# Go to the management area of your radio station in Radiojar, click on Tools and then Directories.
# You can fill-in the Partner ID, Partner Key and Station ID as given to you by TuneIn broadcaster
# support (Including an "s" before the Station ID)  and click on Save:

# https://cms.tunein.com/broadcasters/api/
def brodcast_song_details(target_station):

if __name__ == '__main__':
    target_station = 'wozo'
    get_listeners(target_station):


