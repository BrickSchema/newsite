---
title: Tools and Downloads
---

## Brick Distribution

The Brick ontology is distributed as a set of [Turtle][15] files.
Turtle is a compact textual format that is understood by most Semantic Web tools.

{{< releases "table table-striped table-bordered" "width: 100%; max-width: 100%;" >}}

As of 1.4.0, the `Brick` download above contains the Brick and RealEstateCore ontologies in the same file.
Prior to version 1.4.0, the `Brick` downloads above only contain the core Brick ontology and require the use of other ontologies to fully validate any models.
See the [Brick distributions](https://docs.brickschema.org/lifecycle/distribution.html) page for more information.
Other Brick distributions (`Brick+imports.ttl`, `Brick-only.ttl`, `Brick+extensions.ttl` and `imports.zip`) are available by clicking on the "Changelog" link above.

## Brick Tools
---

Coming soon...

## Reference Brick Models


### Mortardata Brick Models

These models are anonymized representations of real buildings, as originally published in the [Mortar][18] paper.

{{< listfiles path="static/ttl/mortar/" >}}

### Original Brick Reference Models

These five models were distributed with the original Brick paper as representative examples of how Brick can be used to model real buildings.
**They use early, unsupported versions of Brick and are not guaranteed to be up-to-date with the latest version of the schema.**
For an in-depth discussion of the creation and evaluation of these Brick models, please refer to the [BuildSys 2016][6] and [Applied Energy 2018][5] papers.

| Building                           | Location                 | BMS                      | Built | Sq Ft   | Points | Relationships | Classified |
|------------------------------------|--------------------------|--------------------------|-------|---------|--------|---------------|------------|
| [Soda Hall][10]                    | Berkeley, CA             | Barrington Systems       | 1994  | 110,565 | 1,586  | 1,939         | **98.7%**  |
| [Gates Hillman Center][11]         | Pittsburgh, PA, USA      | Automated Logic Controls | 2009  | 217,000 | 8,292  | 35,693        | **99%**    |
| [Rice Hall][12]                    | Charlottesville, VA, USA |                          | 2011  | 100,000 | 1,300  | 2,158         | **98.5%**  |
| [Engineering Building Unit 3B][13] | San Diego, CA, USA       | Johnson Controls         | 2004  | 150,000 | 4,594  | 8,383         | **96%**    |
| [Green Tech House][14]             | Vejle, Denmark           | Niagara                  | 2014  | 38,000  | 956    | 19,086        | **98.8%**  |

- **Points**: the number of BMS points contained in the model
- **Relationships**: the number of relationships contained in the model
- **Classified**: the percentage of points classified with Brick

## Academic Publications
---

#### 2020

[Shepherding Metadata Through the Building Lifecycle][30]
Gabe Fierro, Anand Krishnan Prakash, Cory Mosiman, Marco Pritoni, Paul Raftery, Michael Wetter, David E Culler. In Proceedings of the 7th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys 2020). November 18, 2020, Virtual Event.
DOI: https://doi.org/10.1145/3408308.3427627

[Demo Abstract: Interactive Metadata Integration with Brick][31]
Gabe Fierro, Anand Krishnan Prakash, Cory Mosiman, Marco Pritoni, Paul Raftery, Michael Wetter, David E Culler. In Proceedings of the 7th ACM International Conference on Systems for Energy-Efficient Buildings, Cities, and Transportation (BuildSys 2020). November 18, 2020, Virtual Event.
DOI: https://doi.org/10.1145/3408308.3431125

[Formalizing Tag-Based Metadata with the Brick Ontology][29].
Gabe Fierro, Jason Koh, Shreyas Nagare, Xiaolin Zang, Yuvraj Agarwal, Rajesh K. Gupta, and David E. Culler. Frontiers in Built Environment, Vol 6 (September 2020).
DOI: https://doi.org/10.1145/3360322.3360862

#### 2019

[Who can Access What, and When?: Understanding Minimal Access Requirements of Building Applications][25].
Jason Koh, Dezhi Hong, Shreyas Nagare, Sudershan Boovaraghavan, Yuvraj Agarwal, and Rajesh K. Gupta. In Proceedings of the 6th ACM International Conference on Systems for Energy-Efficient Buildings, Cities and Transportation (BuildSys 2019). November 10, 2019, New York, NY, USA.
DOI: https://doi.org/10.1145/3360322.3360862

[Beyond a House of Sticks: Formalizing Metadata Tags with Brick][22].
Gabe Fierro, Jason Koh, Yuvraj Agarwal, Rajesh K. Gupta, and David E. Culler. In Proceedings of the 6th ACM International Conference on Systems for Energy-Efficient Buildings, Cities and Transportation (BuildSys 2019). November 10, 2019, New York, NY, USA.
DOI: https://doi.org/10.1145/3360322.3360862

[Dataset: An Open Dataset and Collection Tool for BMS Point Labels][23].
Gabe Fierro, Sriharsha Guduguntla, and David E. Culler. In Proceedings of the 2nd Workshop on Data Acquisition To Analysis (DATA 2019). November 13-14, 2019, New York, NY, USA.
DOI: https://doi.org/10.1145/3360322.3360862

#### 2018

[Brick: Metadata Schema for Portable Smart Building Applications][5].
Bharathan Balaji, Arka Bhattacharya, Gabriel Fierro, Jingkun Gao, Joshua Gluck, Dezhi Hong, Aslak Johansen, Jason Koh, Joern Ploennigs, Yuvraj Agarwal, Mario Berges, David Culler, Rajesh Gupta, Mikkel Baun Kjærgaard, Mani Srivastava, and Kamin Whitehouse. Applied Energy 226 (2018) 1273-1292.
DOI: https://doi.org/10.1016/j.apenergy.2018.02.091

[A Large-scale Evaluation of Automated Metadata Inference Approaches on Sensors from Air Handling Units][26].
Jingkun Gao, Mario Bergés. Advanced Engineering Informatics (2018) Volume 37, Pages 14-30
DOI: https://doi.org/10.1016/j.aei.2018.04.010

[Design and Analysis of a Query Processor for Brick][17].
Gabe Fierro and David E. Culler. ACM Transactions on Sensor Networks 14, 3-4, Article 18 (November 2018), 25 pages.
DOI: https://doi.org/10.1145/3199666

[Mortar: An Open Testbed for Portable Building Analytics][18].
Gabe Fierro, Marco Pritoni, Moustafa AbdelBaky, Paul Raftery, Therese Peffer, Greg Thomson, and David E. Culler. In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).
DOI: https://doi.org/10.1145/3276774.3276796

[Scrabble: Transferrable Semi-Automated Semantic Metadata Normalization Using Intermediate Representation][19].
Jason Koh, Bharathan Balaji, Dhiman Sengupta, Julian McAuley, Rajesh Gupta, and Yuvraj Agarwal.  In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).
DOI: https://doi.org/10.1145/3276774.3276795

[Plaster: an Integration, Benchmark, and Development Framework for Metadata Normalization Methods][20].
Jason Koh, Dezhi Hong, Rajesh Gupta, Kamin Whitehouse, Hongning Wang, and Yuvraj Agarwal. In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).
DOI: https://doi.org/10.1145/3276774.3276794
[Plaster: an Integration, Benchmark, and Development Framework for Metadata Normalization Methods][20].
Jason Koh, Dezhi Hong, Rajesh Gupta, Kamin Whitehouse, Hongning Wang, and Yuvraj Agarwal. In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).
DOI: https://doi.org/10.1145/3276774.3276794

#### 2017

[HodDB: a Query Processor for Brick][16].
Gabe Fierro, David E. Culler. In Proceedings of the 4th ACM International Conference on Systems for Energy-Efficient Built Environment (BuildSys 2017).
DOI: https://doi.org/10.1145/3137133.3141449

#### 2016

[Brick: Towards a Unified Metadata Schema For Buildings][6].
Bharathan Balaji, Arka Bhattacharya, Gabriel Fierro, Jingkun Gao, Joshua Gluck, Dezhi Hong, Aslak Johansen, Jason Koh, Joern Ploennigs, Yuvraj Agarwal, Mario Berges, David Culler, Rajesh Gupta, Mikkel Baun Kjærgaard, Mani Srivastava, and Kamin Whitehouse. In Proceedings of the 3rd ACM International Conference on Systems for Energy-Efficient Built Environments (BuildSys 2016).
DOI: https://doi.org/10.1145/2993422.2993577

[Demo Abstract: Portable Queries Using the Brick Schema for Building Applications][8].
Bharathan Balaji, Arka Bhattacharya, Gabriel Fierro, Jingkun Gao, Joshua Gluck, Dezhi Hong, Aslak Johansen, Jason Koh, Joern Ploennigs, Yuvraj Agarwal, Mario Berges, David Culler, Rajesh Gupta, Mikkel Baun Kjærgaard, Mani Srivastava, and Kamin Whitehouse. In Proceedings of the 3rd ACM International Conference on Systems for Energy-Efficient Built Environments (BuildSys 2016).
DOI: https://doi.org/10.1145/2993422.2996411

#### 2015

[Short Paper: Analyzing Metadata Schemas for Buildings —The Good, The Bad, and The Ugly][21].
Arka Bhattacharya, Joern Ploennigs, and David Culler. 2015. Short Paper: Analyzing Metadata Schemas for Buildings: The Good, the Bad, and the Ugly. In Proceedings of the 2nd ACM International Conference on Embedded Systems for Energy-Efficient Built Environments (BuildSys 2015).
DOI: https://doi.org/10.1145/2821650.2821669

## White Papers

[White Paper | Brick Schema: Building Blocks for Smart Buildings](https://www.memoori.com/wp-content/uploads/2016/06/Brick_Schema_Whitepaper.pdf)
Memoori 2019

[Leaflet | Brick : Metadata Schema for Buildings for Building Applications][9]

## Presentations

#### 2019

[Why Brick is a Game Changer for Smart Buildings][24]. Memoori Webinar 2019

[Writing Portable Building Analytics with the Brick Metadata Schema](files/acm-e-energy-2019-portable-brick.pdf). Presented at ACM E-Energy 2019

#### 2016

[Brick: Towards a Unified Metadata Schema For Buildings][7]. Presented at BuildSys 2016


[1]: /schema/1.0.3/Brick.ttl
[2]: /schema/1.0.3/BrickFrame.ttl
[3]: /schema/1.0.3/BrickTag.ttl
[4]: /schema/1.0.3/BrickUse.ttl
[5]: /papers/Brick-AppliedEnergy-2018-Balaji.pdf
[6]: /papers/Brick-BuildSys-2016-Balaji.pdf
[7]: /papers/Brick_BuildSys_Presentation.pdf
[8]: /papers/DemoBrick-BuildSys-2016-Balaji.pdf
[9]: https://brickschema.org/docs/Brick-Leaflet.pdf
[10]: /ttl/old/soda_brick.ttl
[11]: /ttl/old/ghc_brick.ttl
[12]: /ttl/old/rice_brick.ttl
[13]: /ttl/old/ebu3b_brick.ttl
[14]: /ttl/old/gtc_brick.ttl
[15]: https://www.w3.org/TR/turtle/
[16]: /papers/HodDB-BuildSys-2017-Fierro.pdf
[17]: /papers/HodDB-TOSN-2018-Fierro.pdf
[18]: /papers/Mortar-BuildSys-2018-Fierro.pdf
[19]: /papers/Scrabble-BuildSys-2018-Koh.pdf
[20]: /papers/Plaster-BuildSys-2018-Koh.pdf
[21]: /papers/MetadataGoodBadUgly-BuildSys-2015-Bhattacharya.pdf
[22]: /papers/HouseOfSticks-BuildSys-2019-Fierro.pdf
[23]: /papers/BuildingMetadataDataset-DATA-2019-Fierro.pdf
[24]: /papers/Brick_Memoori_Webinar_Presentation.pdf
[25]: /papers/WhoWhatWhen-BuildSys-2019-Koh.pdf
[26]: /papers/Advanced-Engineering-Informatics-2018-Gao.pdf
[27]: /schema/1.1/Brick.ttl
[28]: https://github.com/BrickSchema/Brick/releases/download/nightly/Brick.ttl
[29]: /papers/Fierro_Frontier20_Formalizing.pdf
[30]: /papers/shepherding2020fierro.pdf
[31]: /papers/interactive2020fierro.pdf
[32]: /schema/1.1.1/Brick.ttl
[33]: /schema/1.2.0/Brick.ttl
[34]: /tools
[35]: /schema/1.2.1/Brick.ttl
[36]: /schema/1.3.0/Brick.ttl
[37]: /schema/1.4.0/Brick.ttl
