import requests
import numpy
import time
import speedtest

# --------------FUNCTIONS-----------------
def get_elevation(x, y, api_key):
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    params = {"locations": f"{y},{x}", "key": api_key}
    retries = 10
    while retries > 0:
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                results = response.json()
                if "results" in results and len(results["results"]) > 0:
                    return results["results"][0]["elevation"]
                else:
                    return None
            else:
                continue
        except Exception as e:
            continue
        retries -= 1
        time.sleep(0.25)  # Wait for 0.25 second before retrying
    return None
# ---------------- END OF FUNCTIONS -------------

t = []
speed = []

def main():
    api_key = "AIzaSyDre-zTXWW6k6GLt2PSOep0Czfb3LbI-eM"  
    coordinates = numpy.loadtxt(r'Lead Airplane.txt', delimiter=',')
    elevations = []
    st = speedtest.Speedtest()
    
    # Initialize counter for API call timing
    api_calls_made = time.time()
    max_calls_per_sec = 100  # Limit to 100 API calls per second
    
    for lon, lat in coordinates:
        download_speed = st.download() * 10e-6  # in Mega bits per second
        upload_speed = st.upload() * 10e-6     # in Mega bits per second
        speed.append((download_speed, upload_speed))
        start_time = time.time()
        elevations.append(get_elevation(lon, lat, api_key))
        stop_time = time.time()
        t.append(stop_time - start_time)
        if t[-1] < 60/6000:
            time.sleep((60/6000)-t[-1])
    
    data = numpy.column_stack((t, speed, elevations))
    numpy.savetxt("Google Elevations (Lead Airplane).txt", data, delimiter=',')

if __name__ == "__main__":
    main()