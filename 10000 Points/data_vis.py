import numpy
import plotly.graph_objects
import pandas

polygon_bounds = [
    (-122.6857577567847, 48.94030241711934), 
    (-122.6063857776295, 48.37873410006298),
    (-122.8906994282396, 48.00958354081713),
    (-124.2706751004853, 48.18775023007547),
    (-124.6025462974804, 48.32769283812108),
    (-124.1947126313303, 47.33927610426709),
    (-123.9390245246214, 46.57049015689527),
    (-123.829211380742, 45.52745002831814),
    (-123.9438860035534, 44.98829471403428),
    (-124.0380413142563, 44.46089256942287),
    (-124.0803979504582, 43.868138326421),
    (-124.2457544969574, 43.36300783353873),
    (-124.3233146892578, 43.29596431914504),
    (-124.4785271784322, 42.83741787025245),
    (-124.2825639827456, 42.43931382005313),
    (-124.4018719786805, 42.38620304530941),
    (-124.3553875083492, 42.28576698206884),
    (-124.2925213993602, 42.12181964529633),
    (-124.1817015089088, 41.98991977159308),
    (-124.1903996506, 41.78879474204144),
    (-124.0213526448629, 41.59595460503566),
    (-124.0399779080645, 41.47456260278828),
    (-124.0645168077894, 41.25252971756922),
    (-124.1065512642987, 40.84241284675053),
    (-124.3488035468761, 40.49833216634048),
    (-124.2779985748658, 40.26796836420275),
    (-123.8409056810385, 39.87291886626242),
    (-123.7042362947764, 39.55662803161388),
    (-123.7660936777351, 39.38094988029678),
    (-123.7156460805907, 39.17704131370015),
    (-123.6435527372606, 38.92258124543211),
    (-123.4181740458788, 38.72396716957437),
    (-122.782563130777, 38.21384914047344),
    (-122.1294040063648, 37.22008599851132),
    (-121.4093303463164, 36.5068735257974),
    (-121.665013681228, 36.22561890055759),
    (-120.3723552027148, 35.02493404527524),
    (-119.4390458636424, 34.37822554685411),
    (-118.3423227229954, 33.97431252285308),
    (-117.5351953188449, 33.45134431122992),
    (-116.9576755588616, 32.59098499329831),
    (-114.6952557365815, 32.73291169186425),
    (-114.7983558365671, 32.49537437942514),
    (-111.0752354442178, 31.35315744844732),
    (-108.2257665886121, 31.35247348255265),
    (-108.226711559247, 31.79727909627395),
    (-106.5032773144487, 31.80171742337307),
    (-104.8622904922473, 30.67042114009246),
    (-104.4526716212046, 29.67734994813125),
    (-103.1654150238693, 29.00977910556433),
    (-102.8865929326169, 29.52844309847122),
    (-102.5085093410009, 30.0289788287427),
    (-101.9137474601914, 29.83246081388085),
    (-101.3295026334242, 29.89135185122205),
    (-100.2292137350317, 28.74046396967245),
    (-99.36668565707885, 27.50278544200299),
    (-98.89022315020614, 26.48866764514025),
    (-97.62897857843321, 26.10245732905449),
    (-97.26857152710386, 26.0428016809723),
    (-97.55182153329876, 27.17205883181966),
    (-96.95302674184143, 28.48331290514125),
    (-95.60309187087094, 28.99639646243347),
    (-94.41977974381646, 29.72455420857754),
    (-93.25336748883939, 29.90768436735205),
    (-92.38965672151679, 29.60875778814559),
    (-91.52397751691386, 29.72252893698037),
    (-90.79362865704826, 29.20358714789191),
    (-89.92572559487735, 29.36464718445728),
    (-89.82771586842108, 30.22798035282696),
    (-89.02964398493869, 30.53135614509596),
    (-88.28046297314194, 30.56949632049413),
    (-87.94351310679404, 30.90451847424194),
    (-87.65771212023658, 30.42443318890987),
    (-86.39981593130629, 30.59119947397803),
    (-85.21649221250951, 29.94783658129025),
    (-84.26359570550835, 30.23171718787472),
    (-83.46849935349719, 29.93169534174766),
    (-82.99673372296633, 29.37563936307684),
    (-82.40321375690503, 28.99396989465947),
    (-82.59332070038707, 27.97141456463135),
    (-82.13391713043437, 26.98875988542579),
    (-81.13004591626553, 25.70065975167062),
    (-80.92435705414634, 25.22081920888297),
    (-80.11730166274701, 26.27980003626645),
    (-80.45509617523395, 27.70429467193387),
    (-81.11385483922007, 29.18179590815336),
    (-81.6502712094686, 30.61636720908847),
    (-81.38441027650913, 31.71234524266184),
    (-80.28553515125478, 32.73406511558362),
    (-79.14328531779184, 33.66990236701342),
    (-77.68814984960954, 34.50262413935241),
    (-76.59396786339445, 34.88744382629207),
    (-75.53855540004561, 35.28159120881678),
    (-75.7939600558164, 36.08797835019119),
    (-76.30914716109081, 36.97517203338084),
    (-76.31831080290854, 37.83171419670166),
    (-76.64565740963378, 39.07998013504505),
    (-75.60384114131124, 39.58137044153423),
    (-74.68256502955521, 40.14007692387181),
    (-73.88571234310638, 40.89788194874841),
    (-72.53977831536656, 41.47818813333822),
    (-72.340682273572, 41.32086543233215),
    (-71.79882874333856, 41.39990023030016),
    (-70.9902752311832, 41.69039570261655),
    (-70.88803142286075, 42.18626903734636),
    (-70.99646461660917, 42.64807863132841),
    (-70.32169673387341, 43.69148885953908),
    (-67.74024093730773, 44.52771261381348),
    (-68.15768919042978, 47.24698480497536),
    (-68.89319710047234, 47.09726357783171),
    (-69.24222653716879, 47.35669654855155),
    (-69.81790163987397, 46.49313263054424),
    (-70.58509991954104, 45.28214937454239),
    (-71.50461043741819, 44.96354461448273),
    (-74.87149924428716, 44.93730121654532),
    (-76.94761177286813, 43.43709929543185),
    (-78.5223972160166, 43.56909203696299),
    (-78.92120950422279, 42.57654077431656),
    (-82.58602916632064, 41.36106051998156),
    (-83.68561009344978, 42.03132187476119),
    (-82.23458091756513, 43.56073803819706),
    (-82.58274441285414, 45.27799069475846),
    (-83.88094965347054, 45.92145107682679),
    (-85.55908445111375, 46.86915732684927),
    (-87.92944465328, 47.93420746033193),
    (-89.19396153335214, 47.84653526215115),
    (-92.04471449936482, 48.02055765455885),
    (-94.95940802025396, 48.63234785449168),
    (-95.85147389168088, 48.82031354014643),
    (-104.0283821438888, 48.90304297129961),
    (-111.5698579001361, 48.83306138177304),
    (-118.8629292046195, 48.85599424518316),
    (-122.6857577567847, 48.94030241711934)
]

poly_lons, poly_lats = zip(*polygon_bounds)

poly_lons += (poly_lons[0],)
poly_lats += (poly_lats[0],)

coords = numpy.loadtxt('Generated Coordinates (US).txt', delimiter = ',')
US = pandas.DataFrame(coords, columns = ["Longitudes", "Latitudes"])

points_trace = plotly.graph_objects.Scattermapbox(lat=US['Latitudes'], lon=US['Longitudes'], mode='markers', marker=plotly.graph_objects.scattermapbox.Marker(size=4,color='blue',), name='Generated Points', showlegend=False)

polygon_trace = plotly.graph_objects.Scattermapbox(lat=poly_lats, lon=poly_lons, mode='lines', line=dict(width=2,color='red'), fill='toself', name='Polygon', showlegend=False)

coords = numpy.loadtxt('Generated Coordinates (US).txt', delimiter = ',')
US = pandas.DataFrame(coords, columns = ["Longitudes", "Latitudes"])
fig = plotly.graph_objects.Figure(data=[points_trace, polygon_trace])
fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat=sum(poly_lats) / len(poly_lats), mapbox_center_lon=sum(poly_lons) / len(poly_lons), mapbox_zoom=3.2, margin={"r":0, "t":0, "l":0, "b":0}, showlegend=False)
fig.show()

import numpy
import plotly.graph_objects
import pandas

polygon_bounds = [
    (-124.1457962258144, 41.96059373562517),  
    (-123.963818736896, 41.25391418834189),  
    (-124.0885042781135, 40.70046340260023),  
    (-124.3416817116918, 40.44577369859456),  
    (-123.7505546170717, 39.81453235070233),  
    (-123.5888745965428, 39.02514983766446),  
    (-122.6505140172602, 37.98980571914052),  
    (-121.9757593526848, 37.01604849052753),  
    (-121.773954042055, 36.86534537792443),  
    (-121.7908051646933, 36.61933286246167),  
    (-121.904638070344, 36.5376837809553),  
    (-121.8341917031879, 36.29484187110238),  
    (-121.5218585785659, 36.05633364092778),  
    (-121.4310298230324, 35.89062761019846),  
    (-121.3033897242646, 35.77379859977839),  
    (-121.2730150214266, 35.67676225282321),  
    (-121.1557620787284, 35.65528176458741),  
    (-121.0763546656765, 35.54955886062816),  
    (-120.9954643731783, 35.47683346570075),  
    (-120.8851755252502, 35.45469274335255),  
    (-120.8383817867508, 35.36764085134074),  
    (-120.8790130363124, 35.26048614347122),  
    (-120.7670965413103, 35.18405497555676),  
    (-120.6623182520674, 35.1878928371035),  
    (-120.6124251386862, 35.09567528182586),  
    (-120.6417423875531, 34.92277755170876),  
    (-120.5977626537323, 34.84950765558425),  
    (-120.6164560093883, 34.76270089495072),  
    (-120.5853431184159, 34.6990249473347),  
    (-120.6076948712044, 34.57966082500079),  
    (-120.5018423256977, 34.52657175999172),  
    (-120.4568970622494, 34.47215114231101),  
    (-120.0838298912835, 34.48157302958067),  
    (-119.8663006339081, 34.43404734556366),  
    (-119.5610124004119, 34.42851813524393),  
    (-119.3507858951635, 34.31913901193649),  
    (-119.2597913647989, 34.2655013853886),  
    (-119.2088310310764, 34.16903244838645),  
    (-119.1121092386588, 34.11623018100853),  
    (-118.9229357691671, 34.05780840509306),  
    (-118.8015557815758, 34.0283481732067),  
    (-118.6461435168036, 34.04675224182908),  
    (-118.5054471629528, 34.03873629390065),  
    (-118.4237726887629, 33.9252567388339),  
    (-118.3821159583936, 33.82842182284671),  
    (-118.4019167731822, 33.76015135644744),  
    (-118.3078801624937, 33.72483502125385),  
    (-118.1662770124961, 33.77121432005115),  
    (-118.0338587293819, 33.71009135749661),  
    (-117.8993685032637, 33.61007559700891),  
    (-117.766124633827, 33.53626455135628),  
    (-117.7108345064862, 33.47762531259836),  
    (-117.6550751781046, 33.45843097718355),  
    (-117.5790563752013, 33.38996817737633),  
    (-117.4786332289673, 33.32298077910827),  
    (-117.3813814946438, 33.20425680352247),  
    (-117.3138679675955, 33.1028249622502),  
    (-117.26873516106, 32.9928165165054),  
    (-117.2476770792069, 32.895182391015),  
    (-117.2546170106352, 32.84146277463701),  
    (-117.2758976868257, 32.83837095393333),  
    (-117.2533376821706, 32.79646461534896),  
    (-117.2148182222034, 32.69416246213953),  
    (-117.1501642490843, 32.65422662294998),  
    (-117.1164298761331, 32.53956526026415),  
    (-114.7062133921145, 32.74378301697468),  
    (-114.7331071612381, 33.39649660137),  
    (-114.2512071160101, 34.30288666669938),  
    (-114.5940585220133, 34.70955813420556),  
    (-114.7412145125004, 35.00975564950367),  
    (-120.1474798915689, 38.94215521683266),  
    (-120.0878453305023, 41.94395312691508),  
    (-124.1457962258144, 41.96059373562517),
]

poly_lons, poly_lats = zip(*polygon_bounds)

poly_lons += (poly_lons[0],)
poly_lats += (poly_lats[0],)

coords = numpy.loadtxt('Generated Coordinates (California).txt', delimiter = ',')
California = pandas.DataFrame(coords, columns = ["Longitudes", "Latitudes"])

points_trace = plotly.graph_objects.Scattermapbox(lat=California['Latitudes'], lon=California['Longitudes'], mode='markers', marker=plotly.graph_objects.scattermapbox.Marker(size=2,color='blue',), name='Generated Points', showlegend=False)

polygon_trace = plotly.graph_objects.Scattermapbox(lat=poly_lats, lon=poly_lons, mode='lines', line=dict(width=2,color='red'), fill='toself', name='Polygon', showlegend=False)


fig = plotly.graph_objects.Figure(data=[points_trace, polygon_trace])
fig.update_layout(mapbox_style="open-street-map", mapbox_center_lat=sum(poly_lats) / len(poly_lats), mapbox_center_lon=sum(poly_lons) / len(poly_lons), mapbox_zoom=4, margin={"r":0, "t":0, "l":0, "b":0}, showlegend=False)
fig.show()

Google_US = numpy.loadtxt('Google Elevations (US).txt', delimiter = ',')
google_df = pandas.DataFrame(Google_US, columns=['Google Time', 'Google Upload Speed', 'Google Download Speed', 'Google Elevation'])
US[['Google Time', 'Google Upload Speed', 'Google Download Speed', 'Google Elevation']] = google_df[['Google Time', 'Google Upload Speed', 'Google Download Speed', 'Google Elevation']]
EPQS_US = numpy.loadtxt('EPQS Elevations (US).txt', delimiter = ',')
epqs_df = pandas.DataFrame(EPQS_US, columns=['EPQS Time', 'EPQS Upload Speed', 'EPQS Download Speed', 'EPQS Elevation'])
US[['EPQS Time', 'EPQS Upload Speed', 'EPQS Download Speed', 'EPQS Elevation']] = epqs_df[['EPQS Time', 'EPQS Upload Speed', 'EPQS Download Speed', 'EPQS Elevation']]
DEM_US = numpy.loadtxt('DEM Elevations (US).txt', delimiter = ',')
dem_df = pandas.DataFrame(DEM_US, columns=['DEM Time', 'DEM Elevation'])
US[['DEM Time', 'DEM Elevation']] = dem_df[['DEM Time', 'DEM Elevation']]

Google_California = numpy.loadtxt('Google Elevations (California).txt', delimiter = ',')
google_df = pandas.DataFrame(Google_California, columns=['Google Time', 'Google Upload Speed', 'Google Download Speed', 'Google Elevation'])
California[['Google Time', 'Google Upload Speed', 'Google Download Speed', 'Google Elevation']] = google_df[['Google Time', 'Google Upload Speed', 'Google Download Speed', 'Google Elevation']]
EPQS_California = numpy.loadtxt('EPQS Elevations (California).txt', delimiter = ',')
epqs_df = pandas.DataFrame(EPQS_California, columns=['EPQS Time', 'EPQS Upload Speed', 'EPQS Download Speed', 'EPQS Elevation'])
California[['EPQS Time', 'EPQS Upload Speed', 'EPQS Download Speed', 'EPQS Elevation']] = epqs_df[['EPQS Time', 'EPQS Upload Speed', 'EPQS Download Speed', 'EPQS Elevation']]
DEM_California = numpy.loadtxt('DEM Elevations (California).txt', delimiter = ',')
dem_df = pandas.DataFrame(DEM_California, columns=['DEM Time', 'DEM Elevation'])
California[['DEM Time', 'DEM Elevation']] = dem_df[['DEM Time', 'DEM Elevation']]

import matplotlib.pyplot

matplotlib.pyplot.figure(figsize=(16, 8), dpi=1000)
matplotlib.pyplot.scatter(US.index, US["Google Time"], marker = 'o', s = 0.8, color = 'green', label='Google LLC')
matplotlib.pyplot.scatter(US.index, US["EPQS Time"], marker = 'x', s = 0.8, color = 'blue', label='EPQS')
matplotlib.pyplot.scatter(US.index, US["DEM Time"], marker = 's', s = 0.8, color = 'red', label='DEM')
matplotlib.pyplot.xlabel(f"Query Number", fontname="Times New Roman")
matplotlib.pyplot.ylabel(f"Time Per Query (s)", fontname="Times New Roman")
matplotlib.pyplot.title(f"Method Comparison - Time Per Query vs Query Number - US Testcase", fontname="Times New Roman")
matplotlib.pyplot.minorticks_on()
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(which='both', linewidth=0.8, zorder='0', alpha=0.5)

import matplotlib.pyplot

matplotlib.pyplot.figure(figsize=(16, 8), dpi=1000)
matplotlib.pyplot.scatter(California.index, California["Google Time"], marker = 'o', s = 1, color = 'Green', label='Google LLC')
matplotlib.pyplot.scatter(California.index, California["EPQS Time"], marker = 'x', s = 1, color = 'Blue', label='EPQS')
matplotlib.pyplot.scatter(California.index, California["DEM Time"], marker = 's', s = 1, color = 'Red', label='DEM')
matplotlib.pyplot.xlabel(f"Query Number", fontname="Times New Roman")
matplotlib.pyplot.ylabel(f"Time Per Query (s)", fontname="Times New Roman")
matplotlib.pyplot.title(f"Method Comparison - Time Per Query vs Query Number - California Testcase", fontname="Times New Roman")
matplotlib.pyplot.minorticks_on()
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(which='both', linewidth=0.8, zorder='0', alpha=0.5)
