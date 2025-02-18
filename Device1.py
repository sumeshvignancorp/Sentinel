#!/usr/bin/python
# JSESSIONID=node01k8fak9m7irdsocc56wrineli33.node0; Path=/
# JSESSIONID=node06n02h0l1se1c9zlt82z90raz23.node0; Path=/
import sys
import math
import urllib.request, urllib.parse, urllib.error
import http.client
import time
import random

id = '58974599632'
server = 'sentinel-live.co.uk:5055'
period = 30
step = 0.001
device_speed = 15
driver_id = '400'

waypoints = [[51.48645874869799, -0.5655721776659131],
             [51.48643968563777, -0.5656290314363478],
             [51.4864424089326, -0.5657121254085216],
             [51.486436962342836, -0.5657981349586664],
             [51.486440593402726, -0.5659133002885214],
             [51.486436962342836, -0.5660124299395358],
             [51.486436962342836, -0.5661071862235937],
             [51.486436962342836, -0.566197569140695],
             [51.48643787010782, -0.5662821209018543],
             [51.486440593402726, -0.5663725038189557],
             [51.48644422446237, -0.5664818379928686],
             [51.48644422446237, -0.5665736786989554],
             [51.48644422446237, -0.566592629955767],
             [51.48644422446237, -0.5666728083499697],
             [51.486446947756896, -0.5667442400102595],
             [51.48644876328648, -0.5668244184044623],
             [51.48645148658076, -0.5669191746885202],
             [51.48645784093338, -0.5670168465505491],
             [51.48645602540414, -0.5670941093667808],
             [51.48646419528515, -0.5672428038433024],
             [51.4864687341073, -0.5673127777146066],
             [51.486466918578486, -0.567397329475766],
             [51.48647781175021, -0.5675168681725774],
             [51.486485073863264, -0.5676276601354758],
             [51.486489612683314, -0.5676334912914179],
             [51.48648688939133, -0.5676364068693889],
             [51.48649415150293, -0.5677471988322873],
             [51.48649869032209, -0.5678230038595335],
             [51.48650413690448, -0.5679031822537365],
             [51.48650504466817, -0.5679585782351856],
             [51.486504136904074, -0.5679163023785219],
             [51.48651412230343, -0.5680081430846088],
             [51.4865095834858, -0.5680985260017101],
             [51.48651775335723, -0.5681684998730143],
             [51.486519568883985, -0.5681670420840288],
             [51.48652229217401, -0.5682326425883766],
             [51.48653681638477, -0.568331772239391],
             [51.4865386319108, -0.5683929993767822],
             [51.48654498625128, -0.5684688044040285],
             [51.48655497164171, -0.5685489827982313],
             [51.48656404926748, -0.5686728948619992],
             [51.4865658647924, -0.5687210018985209],
             [51.48657403465374, -0.5688201315495354],
             [51.48658402003778, -0.5689367546683758],
             [51.48660399079936, -0.5690387998973612],
             [51.486611252892274, -0.5691597963831581],
             [51.48663848573825, -0.5693638868438533],
             [51.486687767061476, -0.569786693046604],
             [51.48673463137256, -0.5700990233830032],
             [51.48676805264555, -0.570364315613848],
             [51.48682428971404, -0.570729328175664],
             [51.48687584029925, -0.5710153173993548],
             [51.48690395877571, -0.5712185202688195],
             [51.486934420438935, -0.5713953820255756],
             [51.486978941294794, -0.571594821878939],
             [51.48701174610812, -0.5717754466517964],
             [51.48706329648136, -0.5720087536500704],
             [51.487096101233995, -0.5721780893746243],
             [51.48714530831868, -0.57238505526019],
             [51.48714999470494, -0.5723925812923923],
             [51.48718748577759, -0.5725732060652498],
             [51.487227320008515, -0.5727312527415],
             [51.487278870138034, -0.572941981643167],
             [51.48731636110473, -0.5730925022872148],
             [51.487372597496964, -0.5732919421405781],
             [51.48743117699845, -0.5734951450100427],
             [51.48748272689747, -0.5737209259761143],
             [51.48746632466322, -0.5737246889922156],
             [51.48746866783992, -0.5737133999439121],
             [51.48747804054546, -0.5736832958151025],
             [51.487492099600175, -0.5737133999439121],
             [51.487494442775514, -0.5737397410566204],
             [51.48756708115206, -0.5739692850387934],
             [51.48761160139014, -0.5741461467955495],
             [51.48762566040366, -0.5741724879082578],
             [51.487653778417716, -0.5743117195040021],
             [51.487714700721995, -0.5745111593573655],
             [51.48778733874763, -0.5747105992107289],
             [51.48783654508636, -0.5748724089030801],
             [51.4878880945271, -0.5750492706598365],
             [51.487927928168986, -0.5751057159382477],
             [51.487988850106966, -0.5752901037272061],
             [51.48804977196352, -0.5754594394517599],
             [51.48810132116321, -0.5756287751763137],
             [51.488162242869485, -0.5757529547076532],
             [51.48822082135645, -0.5759298164644094],
             [51.48829111544148, -0.5761179672694692],
             [51.48835203689418, -0.576249672833011],
             [51.48841764452143, -0.5763926674448564],
             [51.48846685017992, -0.5765808182499162],
             [51.48853011451993, -0.576689945716851],
             [51.488560575096784, -0.5767576800066724],
             [51.488619153071994, -0.5768743335058094],
             [51.48855354573472, -0.5767463909583689],
             [51.488560575096784, -0.5767426279422676],
             [51.48855120261378, -0.5767388649261664],
             [51.488584006295895, -0.5767802581032795],
             [51.48859572189095, -0.5767953101676844],
             [51.48853714388564, -0.5767049977812557],
             [51.48860509436482, -0.5768592814414046],
             [51.48863555489158, -0.5769383047795298],
             [51.48863321177483, -0.5769157266829226],
             [51.48863321177483, -0.5769082006507202],
             [51.48875271057406, -0.5771603227295002],
             [51.48880894519471, -0.5773070803574469],
             [51.48887923837303, -0.5774350229048876],
             [51.488928443533354, -0.5775667284684294],
             [51.48893781593884, -0.5775554394201258],
             [51.48900576582086, -0.5777247751446797],
             [51.48908543107083, -0.577867769756525],
             [51.48917446853842, -0.5780070013522693]]

points = []
for i in range(0, len(waypoints)):
    (lat1, lon1) = waypoints[i]
    (lat2, lon2) = waypoints[(i + 1) % len(waypoints)]
    length = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    count = int(math.ceil(length / step))
    for j in range(0, count):
        lat = lat1 + (lat2 - lat1) * j / count
        lon = lon1 + (lon2 - lon1) * j / count
        points.append((lat, lon))


def send(conn, lat, lon, course, speed, alarm, ignition, motion, accuracy, rpm, fuel, driverUniqueId, temperature, di,
         servertime, devicetime, fixtime, armed, protocol):
    params = (('id', id), ('timestamp', int(time.time() * 1000)), ('lat', lat), ('lon', lon), ('bearing', course),
              ('speed', speed), ('di', di), ('servertime', servertime), ('devicetime', devicetime),
              ('fixtime', fixtime), ('armed', armed), ('protocol', protocol))
    if alarm:
        params = params + (('alarm', 'sos'),)
    if armed:
        params = params + (('armed', 'true'),)
    if protocol:
        params = params + (('protocol', 'atlanta'),)
    if ignition:
        params = params + (('ignition', ignition),)
    if motion:
        params = params + (('motion', motion),)
    if accuracy:
        params = params + (('accuracy', accuracy),)
    if rpm:
        params = params + (('rpm', rpm),)
    if fuel:
        params = params + (('fuel', fuel),)
    if driverUniqueId:
        params = params + (('driverUniqueId', driverUniqueId),)
        # if temperature:
    #   params = params + (('temperature', temperature),)
    if di:
        params = params + (('di', di),)
    if servertime:
        params = params + (('servertime', servertime),)
    if devicetime:
        params = params + (('devicetime', devicetime),)
    if fixtime:
        params = params + (('fixtime', fixtime),)
    #        print("##############")
    #        print(urllib.parse.urlencode(params))
    conn.request('GET', '?' + urllib.parse.urlencode(params))
    conn.getresponse().read()


def course(lat1, lon1, lat2, lon2):
    lat1 = lat1 * math.pi / 180
    lon1 = lon1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    lon2 = lon2 * math.pi / 180
    y = math.sin(lon2 - lon1) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
    return (math.atan2(y, x) % (2 * math.pi)) * 180 / math.pi


index = 0
count = 0
cIndex = 0

try:
    conn = http.client.HTTPConnection(server)
except Exception as e:
    print("Exception Device1 Block-1")
    print(e)

while True:
    count += 1
    (lat1, lon1) = points[index % len(points)]
    (lat2, lon2) = points[(index + 1) % len(points)]
    speed = device_speed if (index % len(points)) != 0 else 0
    alarm = (index % 10) != 0
    if index % 10 != 0:
        ignition = 'true'
        motion = 'true'
    else:
        ignition = 'false'
        motion = 'false'
    print(ignition)
    print(motion)
    accuracy = 100 if (index % 10) == 0 else 0
    rpm = random.randint(500, 4000)
    fuel = random.randint(0, 80)
    temperature = random.randint(28, 60)
    driverUniqueId = driver_id if (index % len(points)) == 0 else False
    di = random.randint(0, 1)
    servertime = int(time.time() * 1000)
    devicetime = int(time.time() * 1000)
    fixtime = int(time.time() * 1000)
    armed = (index % len(points)) != 0
    protocol = "atlanta"
    try:
        send(conn, lat1, lon1, course(lat1, lon1, lat2, lon2), speed + random.randint(0, 40), alarm, ignition, motion,
             accuracy, rpm, fuel, driverUniqueId, temperature, di, servertime, devicetime, fixtime, armed, protocol)
    except Exception as e:
        print("Exception Device1 Block-2")
        time.sleep(period)
        conn = http.client.HTTPConnection(server)

    if (count < len(waypoints)):
        time.sleep(period)
        index += 1
    else:
        time.sleep((60 * 7) + 30)
        count = 0
        index = 0
