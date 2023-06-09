import cohere
from cohere.responses.classify import Example
import streamlit as st
from PIL import Image

co = cohere.Client('kxVhnc8p8sLbAYsblZiGAcRi0tPwdoYvYfcXcnkb')

#config header de la page
favicon = Image.open("favi.png")
st.set_page_config(page_title='Sexist hunters', page_icon=favicon)

st.title("Module de détection de propos sexistes")
st.subheader("sur la base du model sentiment analysis de cohere")
st.markdown("Cette application est un module de détection de propos sexiste. Elle peut être utiliser comme filtre avant la publication sur des forums ou des commentaires.")


examples=[
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Nous devrions tous être traités équitablement, peu importe notre sexe." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Les femmes ont autant le droit de réussir professionnellement que les hommes." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Les stéréotypes sexistes sont nuisibles et doivent être combattus." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Les compétences et les réalisations devraient être la seule mesure de notre valeur, pas notre sexe." ," non-sexiste" ),
    Example(" Nous devrions travailler ensemble pour créer un monde plus égalitaire et inclusif." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Nous devons lutter contre toutes les formes de discrimination, y compris la discrimination basée sur le sexe." ," non-sexiste" ),
    Example(" Nous devrions encourager la diversité et l'inclusion dans tous les aspects de notre société." ," non-sexiste" ),
    Example(" Chaque individu mérite d'être respecté et valorisé, indépendamment de son genre." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" Nous devons éduquer les gens sur l'égalité des sexes et la non-discrimination dès le plus jeune âge." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" La diversité est une force et nous devons célébrer les différences de chacun." ," non-sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes sont plus émotives et moins logiques que les hommes." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes sont plus émotives et moins logiques que les hommes." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont plus émotives et moins logiques que les hommes." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes sont plus émotives et moins logiques que les hommes." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes ne devraient pas travailler et devraient se concentrer sur leur rôle de mère." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les hommes sont plus adaptés pour les emplois physiquement exigeants." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les hommes ne peuvent pas être de bons parents parce qu'ils ne sont pas aussi doux et attentionnés que les femmes." ," sexiste" ),
    Example(" Les femmes ne sont pas faites pour les postes de direction car elles sont trop émotives et instables." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont plus émotives et moins logiques que les hommes." ," sexiste" ),
    Example(" Les femmes doivent être plus douces et plus conciliantes pour être respectées." ," sexiste" ),
    Example(" Les femmes sont moins compétentes que les hommes dans les emplois techniques." ," sexiste" ),
    Example(" Les femmes sont plus attirantes dans des tenues provocantes." ," sexiste" ),
    Example(" Les femmes ne sont pas assez fortes pour faire des travaux manuels." ," sexiste" ),
    Example(" Les femmes sont plus émotives et moins logiques que les hommes." ," sexiste" ),
    Example(" Les femmes devraient être plus soumises et moins ambitieuses." ," sexiste" ),
    Example(" Les femmes représentent environ 50% de la population mondiale." ," neutre" ),
    Example(" Dans certaines régions, les femmes portent traditionnellement des vêtements spécifiques." ," neutre" ),
    Example(" Les femmes participent à diverses activités sportives et compétitions." ," neutre" ),
    Example(" Les femmes peuvent être trouvées dans diverses professions à travers le monde." ," neutre" ),
    Example(" Certaines femmes choisissent de porter des cheveux longs, d'autres préfèrent les cheveux courts." ," neutre" ),
    Example(" Les femmes votent et sont élues à des postes politiques dans de nombreux pays." ," neutre" ),
    Example(" Les femmes ont des préférences variées en matière de mode et de style vestimentaire." ," neutre" ),
    Example(" De nombreuses femmes sont impliquées dans la science, la technologie, l'ingénierie et les mathématiques." ," neutre" ),
    Example(" Certaines femmes aiment cuisiner et partager leurs recettes avec d'autres." ," neutre" ),
    Example(" Les femmes sont présentes dans de nombreux genres de musique en tant que musiciennes et chanteuses." ," neutre" ),
    Example(" Les femmes conduisent des voitures, des motos et d'autres types de véhicules." ," neutre" ),
    Example(" Certaines femmes préfèrent vivre en ville tandis que d'autres choisissent la campagne." ," neutre" ),
    Example(" Les femmes voyagent pour le travail, les études ou les loisirs." ," neutre" ),
    Example(" Certaines femmes sont des entrepreneures et dirigent leurs propres entreprises." ," neutre" ),
    Example(" Les femmes ont des compétences linguistiques diverses et parlent différentes langues." ," neutre" ),
    Example(" Certaines femmes choisissent de poursuivre des études supérieures dans divers domaines." ," neutre" ),
    Example(" Les femmes pratiquent diverses formes d'art, comme la peinture, la sculpture ou la photographie." ," neutre" ),
    Example(" Les femmes sont représentées dans diverses œuvres littéraires en tant qu'auteures et personnages." ," neutre" ),
    Example(" Certaines femmes ont des animaux de compagnie et en prennent soin." ," neutre" ),
    Example(" Les femmes participent à des événements sociaux et culturels dans le monde entier." ," neutre" ),
]

inputs=[
  st.text_input("texte à analyser"),
]

if st.button('Analyser'):
    response = co.classify(
        model='large',
        inputs=inputs,
        examples=examples,
    )

    prediction = response.classifications[0].prediction
    confidence = response.classifications[0].confidence

    #print(f"Raw prediction: {prediction}")
    #print(f"String representation: {str(prediction)}")
    prediction = prediction.strip().lower()

    if prediction == 'sexiste':
        st.error(f"votre propos est sexiste et ne peut pas être publié. Veuillez reformuler votre propos.")
    else:
        st.success("Votre propos peut être publié, félicitation !")
