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
# create a function that inputs lat, long, and time span and outputs all lw flux data


class RadiationData:
#Longwave surface flux (FLNS)
    def lw_flux(lat, lon, start_time, end_time, verbose = False):
        lw = open_cesm2le(
            "FLNS",                    # variable name
            component="atm",
            scenario="historical",
            forcing="cmip6",
            time_slice=(start_time, end_time),
            lat=lat,                   # scalar → nearest grid point
            lon=lon,                   # negative °W fine; converted to 0–360 internally
            members=0,                 # 0-based index; None = all members
        )
        lw = lw.load()
        
        if verbose:
            print ("Longwave Surface Flux")
            print ("-----------------------")
            print ("Dimensions:", lw.dims)
            print (lw.coords)
            print ("Shape:", lw.shape)
            print ("Attributes:", lw.attrs)
            print ("-----------------------")

    # SW surface flux (FSNS)
    def sw_flux(lat, lon, start_time, end_time, verbose = False):
        sw = open_cesm2le(
            "FSNS",                    # variable name
            component="atm",
            scenario="historical",
            forcing="cmip6",
            time_slice=(start_time, end_time),
            lat=lat,                   # scalar → nearest grid point
            lon=lon,                   # negative °W fine; converted to 0–360 internally
            members=0,                 # 0-based index; None = all members
        )
        sw = sw.load()
        
        if verbose:
            print ("Longwave Surface Flux")
            print ("-----------------------")
            print ("Dimensions:", sw.dims)
            print (sw.coords)
            print ("Shape:", sw.shape)
            print ("Attributes:", sw.attrs)
            print ("-----------------------")
    
    #Upwelling LW flux at TOA (FLUT)
    def lw_TOA(lat, lon, start_time, end_time, verbose = False):
        lw_top = open_cesm2le(
            "FLUT",                    # variable name
            component="atm",
            scenario="historical",
            forcing="cmip6",
            time_slice=(start_time, end_time),
            lat=lat,                   # scalar → nearest grid point
            lon=lon,                   # negative °W fine; converted to 0–360 internally
            members=0,                 # 0-based index; None = all members
        )
        lw_top = lw_top.load()
        
        if verbose:
            print ("Longwave Surface Flux")
            print ("-----------------------")
            print ("Dimensions:", lw_top.dims)
            print (lw_top.coords)
            print ("Shape:", lw_top.shape)
            print ("Attributes:", lw_top.attrs)
            print ("-----------------------")

    #SW Flux TOA (FSNTOA)
    def sw_TOA(lat, lon, start_time, end_time, verbose = False):
        sw_top = open_cesm2le(
            "FSNTOA",                    # variable name
            component="atm",
            scenario="historical",
            forcing="cmip6",
            time_slice=(start_time, end_time),
            lat=lat,                   # scalar → nearest grid point
            lon=lon,                   # negative °W fine; converted to 0–360 internally
            members=0,                 # 0-based index; None = all members
        )
        sw_top = sw_top.load()
        
        if verbose:
            print ("Longwave Surface Flux")
            print ("-----------------------")
            print ("Dimensions:", sw_top.dims)
            print (sw_top.coords)
            print ("Shape:", sw_top.shape)
            print ("Attributes:", sw_top.attrs)
            print ("-----------------------")


    #To analyze cloud radiative effect 
    #Clear sky LW flux at the surface (FLNSC)
    def lw_flux_clouds(lat, lon, start_time, end_time, verbose = False):
        lw_cld = open_cesm2le(
            "FLNSC",                    # variable name
            component="atm",
            scenario="historical",
            forcing="cmip6",
            time_slice=(start_time, end_time),
            lat=lat,                   # scalar → nearest grid point
            lon=lon,                   # negative °W fine; converted to 0–360 internally
            members=0,                 # 0-based index; None = all members
        )
        lw_cld = lw_cld.load()
        
        if verbose:
            print ("Longwave Surface Flux")
            print ("-----------------------")
            print ("Dimensions:", lw_cld.dims)
            print (lw_cld.coords)
            print ("Shape:", lw_cld.shape)
            print ("Attributes:", lw_cld.attrs)
            print ("-----------------------")
    
    # clear sky sw flux at the surface
    def sw_flux_clouds(lat, lon, start_time, end_time, verbose = False):
        sw_cld = open_cesm2le(
            "FSNSC",                    # variable name
            component="atm",
            scenario="historical",
            forcing="cmip6",
            time_slice=(start_time, end_time),
            lat=lat,                   # scalar → nearest grid point
            lon=lon,                   # negative °W fine; converted to 0–360 internally
            members=0,                 # 0-based index; None = all members
        )
        sw_cld = sw_cld.load()
        
        if verbose:
            print ("Longwave Surface Flux")
            print ("-----------------------")
            print ("Dimensions:", sw_cld.dims)
            print (sw_cld.coords)
            print ("Shape:", sw_cld.shape)
            print ("Attributes:", sw_cld.attrs)
            print ("-----------------------")


RadiationData.lw_TOA(40, -150, "2000-01", "2005-12", True)

