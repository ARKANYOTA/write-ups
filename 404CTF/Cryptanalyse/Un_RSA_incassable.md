> Bonjour Agent,
>
> Nous avons appris que Hallebarde utilisait le chiffrement RSA pour communiquer! Nous avons pu intercepter un de leur message ci-dessous, ainsi que la clé publique utilisée. Selon nos experts qui sont passés avant, "Le module est trop gros, on ne peut rien faire". Pouvez-vous voir s'ils ont raté quelque chose?


```
Module: 264260849184973464982616810011189432725471679851535970549752992980013685427054130834600835230399904802462965456974947538318213223585436360002292504595152950137188712696208597449140460215140901426523911789537180980494972189978839047835537352914856104135490608512555869141766081593589643441958443651294711541856201978508340915671607277979591968248058399795168563294090427290234733756922544755667413890558324220843460177193246018531280862561066074120654752753002311679435459237771670352371010596105395795940209523309781850979927988566194373203050532192192865140293356042897510103979797577385050030819647066037181  
Exposant: 65537  
Message chiffré: 40110232492214007673187408092050413824057587648366839143339482691859337096033351102276645395275735274322548715598894335826499267358923539936373981416212599523632227239475760261528220077888121552688286380591552417803111794635687206274867498165659330678667435332328065173075710535404048653621228158847748005294255562046654937629633514846123655978199420228460405580305729253303227936760801772396770804796700223239015341586701669475537453700175448572495847377417335800300005252499067811919833639526361733535793115856365357616339193637149185654816751038389408567777725988888990153670326115611236718811592564298263  
```

1. On execute la commande, En Ctrl-C les calculs trop long:
- `python3 RsaCtfTool.py -n 264260849184973464982616810011189432725471679851535970549752992980013685427054130834600835230399904802462965456974947538318213223585436360002292504595152950137188712696208597449140460215140901426523911789537180980494972189978839047835537352914856104135490608512555869141766081593589643441958443651294711541856201978508340915671607277979591968248058399795168563294090427290234733756922544755667413890558324220843460177193246018531280862561066074120654752753002311679435459237771670352371010596105395795940209523309781850979927988566194373203050532192192865140293356042897510103979797577385050030819647066037181 -e 65537 --uncipher 40110232492214007673187408092050413824057587648366839143339482691859337096033351102276645395275735274322548715598894335826499267358923539936373981416212599523632227239475760261528220077888121552688286380591552417803111794635687206274867498165659330678667435332328065173075710535404048653621228158847748005294255562046654937629633514846123655978199420228460405580305729253303227936760801772396770804796700223239015341586701669475537453700175448572495847377417335800300005252499067811919833639526361733535793115856365357616339193637149185654816751038389408567777725988888990153670326115611236718811592564298263`
2. On obtient la ligne:
- utf-8 : 404CTF{F41t35_4tt3t10n5_4v3c_l3_R54}

| `404CTF{F41t35_4tt3t10n5_4v3c_l3_R54}` |
|----------------------------------------|