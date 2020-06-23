lines = """FlipThis https://static-cdn.jtvnw.net/emoticons/v1/115844/1.0
TableHere https://static-cdn.jtvnw.net/emoticons/v1/115845/1.0
ScaredyCat https://static-cdn.jtvnw.net/emoticons/v1/115846/1.0
KappaHD https://static-cdn.jtvnw.net/emoticons/v1/115847/1.0
MiniK https://static-cdn.jtvnw.net/emoticons/v1/115848/1.0
PrimeYouDontSay https://static-cdn.jtvnw.net/emoticons/v1/134251/1.0
PrimeUWot https://static-cdn.jtvnw.net/emoticons/v1/134252/1.0
PrimeRlyTho https://static-cdn.jtvnw.net/emoticons/v1/134253/1.0
BagOfMemes https://static-cdn.jtvnw.net/emoticons/v1/426163/1.0
MindManners https://static-cdn.jtvnw.net/emoticons/v1/426167/1.0
PartyPopper https://static-cdn.jtvnw.net/emoticons/v1/426170/1.0
PokBlaziken https://static-cdn.jtvnw.net/emoticons/v1/743872/1.0
PokCharizard https://static-cdn.jtvnw.net/emoticons/v1/743875/1.0
PokGardevoir https://static-cdn.jtvnw.net/emoticons/v1/743884/1.0
PokGengar https://static-cdn.jtvnw.net/emoticons/v1/743886/1.0
PokCroagunk https://static-cdn.jtvnw.net/emoticons/v1/743889/1.0
PokLucario https://static-cdn.jtvnw.net/emoticons/v1/743892/1.0
PokMachamp https://static-cdn.jtvnw.net/emoticons/v1/743895/1.0
PokMaskedpika https://static-cdn.jtvnw.net/emoticons/v1/743899/1.0
PokMewtwo https://static-cdn.jtvnw.net/emoticons/v1/743901/1.0
PokPikachu https://static-cdn.jtvnw.net/emoticons/v1/743904/1.0
PokSuicune https://static-cdn.jtvnw.net/emoticons/v1/743905/1.0
PokWeavile https://static-cdn.jtvnw.net/emoticons/v1/743907/1.0
PokAegislash https://static-cdn.jtvnw.net/emoticons/v1/743910/1.0
PokBraixen https://static-cdn.jtvnw.net/emoticons/v1/743912/1.0
PokChandelure https://static-cdn.jtvnw.net/emoticons/v1/743914/1.0
PokGarchomp https://static-cdn.jtvnw.net/emoticons/v1/743918/1.0
PokSceptile https://static-cdn.jtvnw.net/emoticons/v1/743922/1.0
PokShadowmew https://static-cdn.jtvnw.net/emoticons/v1/743929/1.0
FortOne https://static-cdn.jtvnw.net/emoticons/v1/822112/1.0
FortBush https://static-cdn.jtvnw.net/emoticons/v1/822126/1.0
FortHype https://static-cdn.jtvnw.net/emoticons/v1/822137/1.0
FortLlama https://static-cdn.jtvnw.net/emoticons/v1/822146/1.0
PokBlastoise https://static-cdn.jtvnw.net/emoticons/v1/864143/1.0
PokDarkrai https://static-cdn.jtvnw.net/emoticons/v1/864145/1.0
PokDecidueye https://static-cdn.jtvnw.net/emoticons/v1/864147/1.0
PokEmpoleon https://static-cdn.jtvnw.net/emoticons/v1/864148/1.0
PokScizor https://static-cdn.jtvnw.net/emoticons/v1/864149/1.0"""

final = []
for line in lines.splitlines():
    id = line.split("/v1/",1)[1].split("/",1)[0]
    name = line.split()[0]
    final.append('<img src="https://static-cdn.jtvnw.net/emoticons/v1/'+id+'/2.0" title="'+name+'" alt="'+name+'" height="30px">')
print("\n".join(final))
