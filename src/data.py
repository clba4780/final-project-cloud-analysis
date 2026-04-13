from core import list_variables
from core import open_cesm2le
""" Goal: Load data from the data_access submodule
Variables to access: 
a) 
b) 
.
.
.
"""

"""
Part 1:Accessing
- Access data from data_access
"""

"""
Part 2: cleaning
- handle missing values
- handle conversion (if necessary)
- select time and spatial region
"""

# list of all atmospheric variables
print(list_variables("atm", "historical", "cmip6"))
print(list_variables("atm", "ssp30", "smbb"))


# accessing radiation variable: want to calculate the net radiative flux
# create a function that inputs lat, long, and time span
    # upload the data from that function

def select_data(lat, lon, start_time, end_time):
    da = open_cesm2le(
        "FLNS",                       # variable name
        component="atm",
        scenario="historical",
        forcing="cmip6",
        time_slice=(start_time, end_time),
        lat=lat,                       # scalar → nearest grid point
        lon=lon,                     # negative °W fine; converted to 0–360 internally
        members=0,                      # 0-based index; None = all members
    )
    da.load().plot()
    print (da.dims)
    print (da.coords)
    print (da.shape)
    print (da.attrs)

select_data(40, -105.0, "1990-01", "2000-12")

