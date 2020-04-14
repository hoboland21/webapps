from covid.models import States

STATES= [
"AK","AL","AR","AZ","CA",
"CO","CT","DC","DE","FL",
"GA","HI","IA","ID","IL",
"IN","KS","KY","LA","MA",
"MD","ME","MI","MN","MO",
"MS","MT","NC","ND","NE",
"NH","NJ","NM","NV","NY",
"OH","OK","OR","PA","PR",
"RI","SC","SD","TN","TX",
"UT","VA","VT","WA","WI",
"WV","WY"]

STATE_NAMES = [
("AK","Alaska"),("AL","Alabama"),("AR","Arkansas"),("AZ","Arizona"),("CA","California"),
("CO","Colorado"),("CT","Connecticut"),("DC","Washington D.C"),("DE","Delaware"),("FL","Florida"),
("GA","Georgia"),("HI","Hawaii"),("IA","Iowa"),("ID","Idaho"),("IL","Illinois"),
("IN","Indiana"),("KS","Kansas"),("KY","Kentucky"),("LA","Louisiana"),("MA","Maine"),
("MD","Maryland"),("ME","Maine"),("MI","Michigan"),("MN","Minnesota"),("MO","Missouri"),
("MS","Mississippi"),("MT","Montana"),("NC","North Carolina"),("ND","North Dakota"),("NE","Nebraska"),
("NH","New Hampshire"),("NJ","New Jersey"),("NM","New Mexico"),("NV","Nevada"),("NY","New York"),
("OH","Ohio"),("OK","Oklahoma"),("OR","Oregon"),("PA","Pennsylvania"),("PR","Puerto Rico"),
("RI","Rhode Island"),("SC","South Carolina"),("SD","South Dakota"),("TN","Tennessee"),("TX","Texas"),
("UT","Utah"),("VA","Virginia"),("VT","Vermont"),("WA","Washington"),("WI","Wisconsin"),
("WV","West Virginia"),("WY","Wyoming")]






state_links =   [
      ("http://dhss.alaska.gov/dph/Epi/id/Pages/COVID-19/monitoring.aspx","AK"),
        ("http://alabamapublichealth.gov/infectiousdiseases/2019-coronavirus.html","AL"),
        ("https://www.healthy.arkansas.gov/programs-services/topics/novel-coronavirus","AR"),
        ("https://tableau.azdhs.gov/views/COVID-19Dashboard/COVID-19table?:isGuestRedirectFromVizportal=y&amp;:embed=y","AZ"),
        ("https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/Immunization/nCOV2019.aspx","CA"),
        ("https://covid19.colorado.gov/data","CO"),
        ("https://portal.ct.gov/Coronavirus","CT"),
        ("https://coronavirus.dc.gov/page/coronavirus-data","DC"),
        ("https://coronavirus.delaware.gov/","DE"),
        ("http://floridahealthcovid19.gov","FL"),
        ("https://dph.georgia.gov/covid-19-daily-status-report","GA"),
        ("https://health.hawaii.gov/coronavirusdisease2019/","HI"),
        ("https://idph.iowa.gov/Emerging-Health-Issues/Novel-Coronavirus","IA"),
        ("https://healthandwelfare.idaho.gov/COVID19/tabid/4664/Default.aspx","ID"),
        ("http://www.dph.illinois.gov/topics-services/diseases-and-conditions/diseases-a-z-list/coronavirus","IL"),
        ("https://coronavirus.in.gov/map-test/test.htm","IN"),
        ("http://www.kdheks.gov/coronavirus/index.htm","KS"),
        ("https://chfs.ky.gov/agencies/dph/Pages/covid19.aspx","KY"),
        ("http://ldh.la.gov/coronavirus/","LA"),
        ("https://www.mass.gov/info-details/covid-19-quarantine-and-monitoring","MA"),
        ("https://phpa.health.maryland.gov/Pages/Novel-coronavirus.aspx","MD"),
        ("https://www.maine.gov/dhhs/mecdc/infectious-disease/epi/airborne/coronavirus.shtml","ME"),
        ("https://www.michigan.gov/coronavirus","MI"),
        ("https://www.health.state.mn.us/diseases/coronavirus/situation.html","MN"),
        ("https://health.mo.gov/living/healthcondiseases/communicable/novel-coronavirus/results.php","MO"),
        ("https://msdh.ms.gov/msdhsite/_static/14,0,420.html","MS"),
        ("https://dphhs.mt.gov/publichealth/cdepi/diseases/coronavirusmt/demographics","MT"),
        ("https://www.ncdhhs.gov/covid-19-case-count-nc","NC"),
        ("https://www.health.nd.gov/diseases-conditions/coronavirus/north-dakota-coronavirus-cases","ND"),
        ("http://dhhs.ne.gov/Pages/Coronavirus.aspx","NE"),
        ("https://www.nh.gov/covid19/","NH"),
        ("https://www.nj.gov/health/","NJ"),
        ("https://nmhealth.org/about/erd/ideb/ncov/","NM"),
        ("https://nvhealthresponse.nv.gov/","NV"),
        ("https://coronavirus.health.ny.gov/county-county-breakdown-positive-cases","NY"),
        ("https://coronavirus.ohio.gov/wps/portal/gov/covid-19/","OH"),
        ("https://coronavirus.health.ok.gov/","OK"),
        ("https://www.oregon.gov/oha/PH/DISEASESCONDITIONS/DISEASESAZ/Pages/emerging-respiratory-infections.aspx","OR"),
        ("https://www.health.pa.gov/topics/disease/coronavirus/Pages/Cases.aspx","PA"),
        ("http://www.salud.gov.pr/Pages/coronavirus.aspx","PR"),
        ("https://health.ri.gov/data/covid-19/","RI"),
        ("https://www.scdhec.gov/monitoring-testing-covid-19","SC"),
        ("https://doh.sd.gov/news/Coronavirus.aspx","SD"),
        ("https://www.tn.gov/health/cedep/ncov.html","TN"),
        ("https://www.dshs.state.tx.us/news/updates.shtm#coronavirus","TX"),
        ("https://coronavirus-dashboard.utah.gov","UT"),
        ("http://www.vdh.virginia.gov/surveillance-and-investigation/novel-coronavirus/","VA"),
        ("https://www.healthvermont.gov/response/infectious-disease/2019-novel-coronavirus","VT"),
        ("https://www.doh.wa.gov/emergencies/coronavirus","WA"),
        ("https://www.dhs.wisconsin.gov/outbreaks/index.htm","WI"),
        ("https://dhhr.wv.gov/Coronavirus%20Disease-COVID-19/Pages/default.aspx","WV"),
        ("https://health.wyo.gov/publichealth/infectious-disease-epidemiology-unit/disease/novel-coronavirus/","WY"),
	]

def initialize_state_db() :
    States.objects.all().delete()
    for s in STATES :
        state = States.objects.create(abbrev=s )
        state.save()
    for s in STATE_NAMES :
        smodel = States.objects.get(abbrev=s[0])
        smodel.name = s[1]
        smodel.save()
    for s in state_links :
        smodel = States.objects.get(abbrev=s[1])
        smodel.url = s[0]
        smodel.save()
    