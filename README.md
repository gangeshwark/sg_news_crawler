## Script to crawl all major news channel website in Singapore and SEA.
#### Specifically designed to crawl news related to COVID-19, Coronavirus, 2019-nCoV
1. CNA
2. The Strait Times
3. SCMP
4. Mothership.sg
5. The Guardian
6. The New York Times
7. The Online Citizen
8. The Independent SG
9. Today Online


### To run CNA
`python cna/crawler.py`


### To run Mothership
`python mothership/ms_sel.py`
`python mothership/get_data.py`


### To run The Strait Times

### To run The New York Times
`python parse_archive.py`

### To run The Guardian

### To run The Online Citizen

### To run Today Online

### To run SCMP


## Notes
1. Today Online has no time stamp. Only published date available.
2. Can not crawl from The Independent SG. Auto blocking crawlers.
3. Can only crawl 'Today Online' until Jan 22, 2020

### TODO
- [X] CNA Timestamp
- [X] Strait Times Timestamp
- [X] Mothership Timestamp
- [X] NYT Timestamp
- [ ] TOC Timestamp
- [ ] Combine with manual data
