import matplotlib.pyplot as plt
import seaborn as sns
from gender_novels.corpus import Corpus

def plt_pubyears(years,name_of_data):
    '''
    Creates a histogram displaying the frequency of books that were published within a 20 year 
    period
    :param years: list
    RETURNS a pyplot histogram
    '''
    sns.set_style('ticks')
    ax1=plt.subplot2grid((1,1),(0,0))
    bins=[num for num in range(min(years),max(years)+5,5)]
    plt.hist(years,bins,histtype='bar',rwidth=.8,color='plum')
    plt.xlabel('Year', size=13,weight='bold',color='slategray')
    plt.ylabel('Frequency',size=13,weight='bold',color='slategray')
    plt.title('Publication Year Concentration for '+name_of_data,size=15,weight='bold',
              color='slategray')
    plt.yticks(size=13,color='slategray')
    plt.xticks([i for i in range(min(years),max(years)+9,10)],size=13,color='slategray')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(60)
    plt.subplots_adjust(left=.1,bottom=.18,right=.95,top=.9)
    plt.savefig('date_of_pub_for_'+name_of_data+'.png')

def plt_pubcountries(pub_country,name_of_data):
    '''
    Creates a bar graph displaying the frequency of books that were published in each country
    :param pub_country: list
    RETURNS a pyplot bargraph
    '''
    sns.set_style('ticks')
    ax1=plt.subplot2grid((1,1),(0,0))
    country_counter={}
    for country in pub_country:
        country_counter[country]=country_counter.setdefault(country,0)+1
    x=[country for country in country_counter]
    y=[country_counter[key] for key in country_counter]
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(15)
    plt.bar(x,y,color='plum')
    plt.xlabel('Countries',size=13,weight='bold',color='slategray')
    plt.ylabel('Frequency',size=13,weight='bold',color='slategray')
    plt.title('Country of Publication for '+name_of_data,size=15,color='slategray',weight='bold')
    plt.xticks(color='slategray',size=13)
    plt.yticks(color='slategray',size=13)
    plt.subplots_adjust(left=.1,bottom=.18,right=.95,top=.9)
    plt.savefig('country_of_pub_for_'+name_of_data+'.png')

def plt_gender_breakdown(pub_gender,name_of_data):
    '''
    Creates a pie chart displaying the composition of male and female writers in the data
    :param pub_gender: list
    :param name_of_data: str
    RETURNS a pie chart
    '''
    gendercount={}
    for i in pub_gender:
        gendercount[i]=gendercount.setdefault(i,0)+1
    total=0
    for i in gendercount:
        total+=gendercount[i]
    slices=[gendercount[i]/total for i in gendercount]
    genders=[i for i in gendercount]
    labelgenders=[]
    for i in range(len(genders)):
        labelgenders.append(genders[i]+': ' + str(round(slices[i],2)*100)+'%')
    colors=['slateblue','mediumpurple','plum']
    plt.pie(slices,colors=colors,labels=labelgenders,textprops={'fontsize':15})
    plt.title('Gender Breakdown for '+name_of_data,size=15,color='slategray',weight='bold')
    plt.legend()
    plt.subplots_adjust(left=.1,bottom=.1,right=.9,top=.9)
    plt.savefig('gender_breakdown_for_'+name_of_data+'.png')

if __name__=='__main__':
    pubyears=[]
    pubgender=[]
    pubcountry=[]
    c = Corpus('sample_novels')
    for novel in c.novels:
        pubyears.append(novel.date)
        pubgender.append(novel.author_gender)
        pubcountry.append(novel.country_publication)
    plt_gender_breakdown(pubgender, 'sample novels')
    plt_pubyears(pubyears,'sample novels')
    plt_pubcountries(pubcountry,'sample novels')

