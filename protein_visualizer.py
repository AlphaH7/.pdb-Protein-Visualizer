import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ProteinDraw_1:
    def __init__(self, name):
        cho = [] 
        self.name = name        
        with open(name) as protein:
            for lines in protein:
                if "ATOM   " in lines:
                    lines = lines.split()
                    cho.append(map(float, lines[6:9]))


        x,y,z = zip(*cho)

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot(x,y,z, "o", color='blue')
        ax.axis("off")
        ax.set_title(".pdb file molecular view")
        fig.suptitle("python protein visualizer", fontsize=18)
        plt.show()

class ProteinDraw_2:
    def __init__(self, name_a, name_b):
        cho_a = [] 
        cho_b = [] 
        self.name_a = name_a
        self.name_b = name_b
        with open(name_a) as protein:
            for lines in protein:
                if "ATOM   " in lines:
                    lines = lines.split()
                    cho_a.append(map(float, lines[6:9]))
        
        with open(name_b) as protein:
            for lines in protein:
                if "ATOM   " in lines:
                    lines = lines.split()
                    cho_b.append(map(float, lines[6:9]))

        x,y,z = zip(*cho_a)
        p,q,r = zip(*cho_b)
        fig = plt.figure()
        ax1 = fig.add_subplot(1,2,1, projection='3d')
        ax2 = fig.add_subplot(1,2,2, projection='3d')
        ax1.plot(x,y,z, "o", color='red')
        ax2.plot(p,q,r, "o", color='green')
        ax1.set_title(".pdb file - 1")
        ax2.set_title(".pdb file - 2")
        fig.suptitle("PROTEIN COMPARISION MODULE", fontsize=18)
        plt.show()


contd = 0;


while (contd == 0):                             
    i = raw_input("\n----- Protein Visualizer V_1.0 -----\n a) Enter 1 to display all stored sequences in the bank and visualize one \n b) Enter 2 to enter manually a .pdb file to visualize \n c) Enter 3 to select a pdb file from stored database and compare with a manually entered .pdb protein \n 4) Enter 4 to compare 2 user entered pdb files in PDB COMPARISION MODULE \n\n ")   
    if i == "1":
        chc = 0;
        while (chc == 0):
            print " \n-----Store Protein Sequences-----\n \n 1) Tissue Plasminogen Activator \n 2) Factor VIII (Anti-Haemophilic) \n 3) Dornase\n 4) Alpha Galactosidase \n 5) Eruthropoeitin \n 6) Glucagone \n 7) Alpha Glucosidase \n 8)Hepatitis B Vaccine \n 9) Human Growth Hormone (Somatotropin) \n 10) Insulin (Recombinant type) \n 11) Interferon (AntiViral Protein) \n\n "
            choice = raw_input("Enter the option: ")
            if choice == "1":
                print " Description: \n Tissue plasminogen activator (abbreviated tPA or PLAT) is a protein involved in the breakdown of blood clots. It is a serine protease (EC 3.4.21.68) found on endothelial cells, the cells that line the blood vessels. As an enzyme, it catalyzes the conversion of plasminogen to plasmin, the major enzyme responsible for clot breakdown. Because it works on the clotting system, tPA (such as alteplase, reteplase, and tenecteplase) is used in clinical medicine to treat embolic or thrombotic stroke. Use is contraindicated in hemorrhagic stroke and head trauma. "
                ax = ProteinDraw_1 ("Tissure Plasminogen Activator.pdb")
                  
            if choice == "2":
                print " Description: \n Antihemophilic factor (factor VIII) is a naturally occurring protein in the blood that helps blood to clot. A lack of factor VIII is the cause of hemophilia A. Antihemophilic factor (factor VIII) is used to treat or prevent bleeding in people with hemophilia A."
                ax = ProteinDraw_1 ("Factor VIII.pdb")
                  
            if choice == "3":
                print " Description \n Improving lung function and reducing the risk of respiratory tract infections in patients with cystic fibrosis. Dornase alfa is an enzyme. It works by decreasing the thickness and stickiness of mucus secretions in the airways of cystic fibrosis patients."
                ax = ProteinDraw_1 ("Dornase.pdb")
                  
            if choice == "4":
                ax = ProteinDraw_1 ("Alpha Galactosidase.pdb")
                  
            if choice == "5":
                print " Description: \n Erythropoietin is an essential hormone for red blood cell production. Without it, definitive erythropoiesis does not take place. Under hypoxic conditions, the kidney will produce and secrete erythropoietin to increase the production of red blood cells by targeting CFU-E, proerythroblast and basophilic erythroblast subsets in the differentiation. Erythropoietin has its primary effect on red blood cell progenitors and precursors (which are found in the bone marrow in humans) by promoting their survival through protecting these cells from apoptosis, or cell death."
                ax = ProteinDraw_1 ("Erythropoeitin.pdb")
                  
            if choice == "6":
                print " Description: \n Glucagon is a hormone that causes the liver to release glucose into the blood. It is used to quickly increase blood sugar levels in diabetics with low blood sugar (hypoglycemia). This medication may also be used during certain medical tests. "
                ax = ProteinDraw_1 ("Glucagone.pdb")

            if choice == "7":
                print " Description: \n Alpha-glucosidase inhibitors are oral anti-diabetic drugs used for diabetes mellitus type 2 that work by preventing the digestion of carbohydrates (such as starch and table sugar). Carbohydrates are normally converted into simple sugars (monosaccharides), which can be absorbed through the intestine."
                ax = ProteinDraw_1 ("Glucosidase.pdb")
            
            if choice == "8":
                print " Description: \n This vaccine is used to help prevent infection from the hepatitis B virus. Hepatitis B infection can cause serious problems including liver failure, persistent hepatitis B infection, cirrhosis, and liver cancer. Preventing infection can prevent these problems. Hepatitis B vaccine is a genetically engineered (man-made in the laboratory) piece of the virus. It does not contain live virus, so you cannot get hepatitis from the vaccine. This vaccine works by helping the body produce immunity (through antibody production) that will prevent you from getting infection from hepatitis B virus. "
                ax = ProteinDraw_1 ("Hepatitis C Virus.pdb")
            
            if choice == "9":
                print " Description: \n Human growth hormone (GH) is a substance that controls your body's growth. GH is made by the pituitary gland, located at the base of the brain. GH helps children grow taller (also called linear growth), increases muscle mass, and decreases body fat."
                ax = ProteinDraw_1 ("HGH.pdb")
        
            if choice == "10":
                print " Description: \n Insulin is used to treat a number of diseases including diabetes and its acute complications such as diabetic ketoacidosis and hyperosmolar hyperglycemic states.[3] It is also used along with glucose to treat high blood potassium levels.[3] Insulin was formerly used in a psychiatric treatment called insulin shock therapy."
                ax = ProteinDraw_1 ("Insulin.pdb")
            
            if choice == "11":
                print " Description: \n Interferons (IFNs) are a group of signaling proteins made and released by host cells in response to the presence of several pathogens, such as viruses, bacteria, parasites, and also tumor cells. In a typical scenario, a virus-infected cell will release interferons causing nearby cells to heighten their anti-viral defenses."
                ax = ProteinDraw_1 ("Interferon.pdb")

 
                  
            chc= int(input("\n \n Press 0 to go to view another protein  \n Press 1 to go to the main menu \n"))   

    if i == "2":

         name = raw_input("Enter the filename: ")
         ax = ProteinDraw_1 (name)
                   
        
    if i == "3":

         name = raw_input("Enter the filename: ")
         print " \n-----Store Protein Sequences-----\n \n 1) Tissue Plasminogen Activator \n 2) Factor VIII (Anti-Haemophilic) \n 3) Dornase\n 4) Alpha Galactosidase \n 5) Eruthropoeitin \n 6) Glucagone \n 7) Alpha Glucosidase \n 8)Hepatitis B Vaccine \n 9) Human Growth Hormone (Somatotropin) \n 10)Insulin (Recombinant type) \n 11) Interferon (AntiViral Protein) \n\n "
         chc = 0;
         while (chc == 0):
            choice = raw_input("Enter choice of sequence: ")
            if choice == "1":
                print " Description: \n Tissue plasminogen activator (abbreviated tPA or PLAT) is a protein involved in the breakdown of blood clots. It is a serine protease (EC 3.4.21.68) found on endothelial cells, the cells that line the blood vessels. As an enzyme, it catalyzes the conversion of plasminogen to plasmin, the major enzyme responsible for clot breakdown. Because it works on the clotting system, tPA (such as alteplase, reteplase, and tenecteplase) is used in clinical medicine to treat embolic or thrombotic stroke. Use is contraindicated in hemorrhagic stroke and head trauma. \n"
                ax = ProteinDraw_2 ("Tissure Plasminogen Activator.pdb" , name)
                  
            if choice == "2":
                print " Description: \n Antihemophilic factor (factor VIII) is a naturally occurring protein in the blood that helps blood to clot. A lack of factor VIII is the cause of hemophilia A. Antihemophilic factor (factor VIII) is used to treat or prevent bleeding in people with hemophilia A. \n"
                ax = ProteinDraw_2 ("Factor VIII.pdb" , name)
                  
            if choice == "3":
                print " Description: \n Improving lung function and reducing the risk of respiratory tract infections in patients with cystic fibrosis. Dornase alfa is an enzyme. It works by decreasing the thickness and stickiness of mucus secretions in the airways of cystic fibrosis patients. \n"
                ax = ProteinDraw_2 ("Dornase.pdb", name)
                  
            if choice == "4":
                print " Description: \n"
                ax = ProteinDraw_2 ("Alpha Galactosidase.pdb" , name)
                  
            if choice == "5":
                print " Description: \n Erythropoietin is an essential hormone for red blood cell production. Without it, definitive erythropoiesis does not take place. Under hypoxic conditions, the kidney will produce and secrete erythropoietin to increase the production of red blood cells by targeting CFU-E, proerythroblast and basophilic erythroblast subsets in the differentiation. Erythropoietin has its primary effect on red blood cell progenitors and precursors (which are found in the bone marrow in humans) by promoting their survival through protecting these cells from apoptosis, or cell death.\n"
                ax = ProteinDraw_2 ("Erythropoeitin.pdb" , name)
                  
            if choice == "6":
                print " Description: \n Glucagon is a hormone that causes the liver to release glucose into the blood. It is used to quickly increase blood sugar levels in diabetics with low blood sugar (hypoglycemia). This medication may also be used during certain medical tests."
                ax = ProteinDraw_2 ("Glucagone.pdb" , name)

            if choice == "7":
                print " Description: \n Alpha-glucosidase inhibitors are oral anti-diabetic drugs used for diabetes mellitus type 2 that work by preventing the digestion of carbohydrates (such as starch and table sugar). Carbohydrates are normally converted into simple sugars (monosaccharides), which can be absorbed through the intestine."
                ax = ProteinDraw_2 ("Glucosidase.pdb" , name)
            
            if choice == "8":
                print " Description: \n This vaccine is used to help prevent infection from the hepatitis B virus. Hepatitis B infection can cause serious problems including liver failure, persistent hepatitis B infection, cirrhosis, and liver cancer. Preventing infection can prevent these problems. Hepatitis B vaccine is a genetically engineered (man-made in the laboratory) piece of the virus. It does not contain live virus, so you cannot get hepatitis from the vaccine. This vaccine works by helping the body produce immunity (through antibody production) that will prevent you from getting infection from hepatitis B virus. "
                ax = ProteinDraw_2 ("Hepatitis C Virus.pdb" , name)
            
            if choice == "9":
                print " Description: \n Human growth hormone (GH) is a substance that controls your body's growth. GH is made by the pituitary gland, located at the base of the brain. GH helps children grow taller (also called linear growth), increases muscle mass, and decreases body fat."
                ax = ProteinDraw_2 ("HGH.pdb" , name)
            
            if choice == "10":
                print " Description: \n Insulin is used to treat a number of diseases including diabetes and its acute complications such as diabetic ketoacidosis and hyperosmolar hyperglycemic states.[3] It is also used along with glucose to treat high blood potassium levels.[3] Insulin was formerly used in a psychiatric treatment called insulin shock therapy."
                ax = ProteinDraw_2 ("Insulin.pdb" , name)
            
            if choice == "11":
                print " Description: \n Interferons (IFNs) are a group of signaling proteins made and released by host cells in response to the presence of several pathogens, such as viruses, bacteria, parasites, and also tumor cells. In a typical scenario, a virus-infected cell will release interferons causing nearby cells to heighten their anti-viral defenses."
                ax = ProteinDraw_2 ("Interferon.pdb" , name)

            chc= int(input("\n \n Press 0 to compare again \n Press 1 to go to the main menu \n"))   

    if i == "4":
        name_1 = raw_input("Enter filename 1: ")
        name_2 = raw_input("Enter filename 2: ")
        ax = ProteinDraw_2 (name_1 , name_2)
    


    contd= int(input("Press 0 to proceed to the main menu, \n Hit 1 to exit\n"))   