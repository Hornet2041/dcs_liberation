# Requires Military Aircraft Mod :
# https://www.digitalcombatsimulator.com/en/files/3307071/
#
from dcs.weapons_data import Weapons
        import dcs.task as task
        from dcs.unittype import FlyingType
        from enum import Enum


        class PlaneType(FlyingType):
    pass


class A400M_Atlas(PlaneType):
    id = "A400M_Atlas"
    height = 11.66
    width = 40.4
    length = 29.79
    fuel_max = 20830
    max_speed = 621
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            Airbus = "Airbus"

        class Georgia(Enum):
            Airbus = "Airbus"

        class Venezuela(Enum):
            Airbus = "Airbus"

        class Australia(Enum):
            Airbus = "Airbus"

        class Israel(Enum):
            Airbus = "Airbus"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Airbus = "Airbus"

        class Sudan(Enum):
            Airbus = "Airbus"

        class Norway(Enum):
            Airbus = "Airbus"

        class Romania(Enum):
            Airbus = "Airbus"

        class Iran(Enum):
            Airbus = "Airbus"

        class Ukraine(Enum):
            Airbus = "Airbus"

        class Libya(Enum):
            Airbus = "Airbus"

        class Belgium(Enum):
            Airbus = "Airbus"

        class Slovakia(Enum):
            Airbus = "Airbus"

        class Greece(Enum):
            Airbus = "Airbus"

        class UK(Enum):
            Airbus = "Airbus"

        class Third_Reich(Enum):
            Airbus = "Airbus"

        class Hungary(Enum):
            Airbus = "Airbus"

        class Abkhazia(Enum):
            Airbus = "Airbus"

        class Morocco(Enum):
            Airbus = "Airbus"

        class United_Nations_Peacekeepers(Enum):
            Airbus = "Airbus"

        class Switzerland(Enum):
            Airbus = "Airbus"

        class SouthOssetia(Enum):
            Airbus = "Airbus"

        class Vietnam(Enum):
            Airbus = "Airbus"

        class China(Enum):
            Airbus = "Airbus"

        class Yemen(Enum):
            Airbus = "Airbus"

        class Kuwait(Enum):
            Airbus = "Airbus"

        class Serbia(Enum):
            Airbus = "Airbus"

        class Oman(Enum):
            Airbus = "Airbus"

        class India(Enum):
            Airbus = "Airbus"

        class Egypt(Enum):
            Airbus = "Airbus"

        class TheNetherlands(Enum):
            Airbus = "Airbus"

        class Poland(Enum):
            Airbus = "Airbus"

        class Syria(Enum):
            Airbus = "Airbus"

        class Finland(Enum):
            Airbus = "Airbus"

        class Kazakhstan(Enum):
            Airbus = "Airbus"

        class Denmark(Enum):
            Airbus = "Airbus"

        class Sweden(Enum):
            Airbus = "Airbus"

        class Croatia(Enum):
            Airbus = "Airbus"

        class CzechRepublic(Enum):
            Airbus = "Airbus"

        class GDR(Enum):
            Airbus = "Airbus"

        class Yugoslavia(Enum):
            Airbus = "Airbus"

        class Bulgaria(Enum):
            Airbus = "Airbus"

        class SouthKorea(Enum):
            Airbus = "Airbus"

        class Tunisia(Enum):
            Airbus = "Airbus"

        class Combined_Joint_Task_Forces_Red(Enum):
            Airbus = "Airbus"

        class Lebanon(Enum):
            Airbus = "Airbus"

        class Portugal(Enum):
            Airbus = "Airbus"

        class Cuba(Enum):
            Airbus = "Airbus"

        class Insurgents(Enum):
            Airbus = "Airbus"

        class SaudiArabia(Enum):
            Airbus = "Airbus"

        class France(Enum):
            Airbus = "Airbus"

        class USA(Enum):
            Airbus = "Airbus"

        class Honduras(Enum):
            Airbus = "Airbus"

        class Qatar(Enum):
            Airbus = "Airbus"

        class Russia(Enum):
            Airbus = "Airbus"

        class United_Arab_Emirates(Enum):
            Airbus = "Airbus"

        class Italian_Social_Republi(Enum):
            Airbus = "Airbus"

        class Austria(Enum):
            Airbus = "Airbus"

        class Bahrain(Enum):
            Airbus = "Airbus"

        class Italy(Enum):
            Airbus = "Airbus"

        class Chile(Enum):
            Airbus = "Airbus"

        class Turkey(Enum):
            Airbus = "Airbus"

        class Philippines(Enum):
            Airbus = "Airbus"

        class Algeria(Enum):
            Airbus = "Airbus"

        class Pakistan(Enum):
            Airbus = "Airbus"

        class Malaysia(Enum):
            Airbus = "Airbus"

        class Indonesia(Enum):
            Airbus = "Airbus"

        class Iraq(Enum):
            Airbus = "Airbus"

        class Germany(Enum):
            Airbus = "Airbus"

        class South_Africa(Enum):
            Airbus = "Airbus"

        class Jordan(Enum):
            Airbus = "Airbus"

        class Mexico(Enum):
            Airbus = "Airbus"

        class USAFAggressors(Enum):
            Airbus = "Airbus"

        class Brazil(Enum):
            Airbus = "Airbus"

        class Spain(Enum):
            Airbus = "Airbus"

        class Belarus(Enum):
            Airbus = "Airbus"

        class Canada(Enum):
            Airbus = "Airbus"

        class NorthKorea(Enum):
            Airbus = "Airbus"

        class Ethiopia(Enum):
            Airbus = "Airbus"

        class Japan(Enum):
            Airbus = "Airbus"

        class Thailand(Enum):
            Airbus = "Airbus"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport
    
    class B2_Spirit(PlaneType):
    id = "B2_Spirit"
    group_size_max = 1
    height = 10.36
    width = 41.67
    length = 44.81
    fuel_max = 88450
    max_speed = 1329.84
    chaff = 60
    flare = 30
    charge_total = 120
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    radio_frequency = 127.5

    class Pylon1:
        B2_Mk_82_40 = (1, Weapons.B2_Mk_82_40)
        B2_CBU87_18 = (1, Weapons.B2_CBU87_18)
        B2_CBU_97_18 = (1, Weapons.B2_CBU_97_18)
        B2_GBU_38_40 = (1, Weapons.B2_GBU_38_40)
        B2_GBU_28_4 = (1, Weapons.B2_GBU_28_4)
        B2_GBU_27_4 = (1, Weapons.B2_GBU_27_4)
        B2_AGM_154C_8 = (1, Weapons.B2_AGM_154C_8)
        B_1B_Mk_84_8 = (1, Weapons.B_1B_Mk_84_8)

    class Pylon2:
        B2_Mk_82_40 = (2, Weapons.B2_Mk_82_40)
        B2_CBU87_18 = (2, Weapons.B2_CBU87_18)
        B2_CBU_97_18 = (2, Weapons.B2_CBU_97_18)
        B2_GBU_38_40 = (2, Weapons.B2_GBU_38_40)
        B2_GBU_28_4 = (2, Weapons.B2_GBU_28_4)
        B2_GBU_27_4 = (2, Weapons.B2_GBU_27_4)
        B2_AGM_154C_8 = (2, Weapons.B2_AGM_154C_8)
        B_1B_Mk_84_8 = (2, Weapons.B_1B_Mk_84_8)

    pylons = {1, 2}

    tasks = [task.GroundAttack, task.RunwayAttack, task.PinpointStrike, task.CAS]
    task_default = task.GroundAttack


class C2A_Greyhound(PlaneType):
    id = "C2A_Greyhound"
    group_size_max = 1
    height = 4.85
    width = 24.6
    length = 17.3
    fuel_max = 5624
    max_speed = 625.68
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Georgia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Venezuela(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Australia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Israel(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Combined_Joint_Task_Forces_Blue(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Sudan(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Norway(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Romania(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Iran(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Ukraine(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Libya(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Belgium(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Slovakia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Greece(Enum):
            USN_VRC_30 = "USN VRC-30"

        class UK(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Third_Reich(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Hungary(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Abkhazia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Morocco(Enum):
            USN_VRC_30 = "USN VRC-30"

        class United_Nations_Peacekeepers(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Switzerland(Enum):
            USN_VRC_30 = "USN VRC-30"

        class SouthOssetia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Vietnam(Enum):
            USN_VRC_30 = "USN VRC-30"

        class China(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Yemen(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Kuwait(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Serbia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Oman(Enum):
            USN_VRC_30 = "USN VRC-30"

        class India(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Egypt(Enum):
            USN_VRC_30 = "USN VRC-30"

        class TheNetherlands(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Poland(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Syria(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Finland(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Kazakhstan(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Denmark(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Sweden(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Croatia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class CzechRepublic(Enum):
            USN_VRC_30 = "USN VRC-30"

        class GDR(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Yugoslavia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Bulgaria(Enum):
            USN_VRC_30 = "USN VRC-30"

        class SouthKorea(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Tunisia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Combined_Joint_Task_Forces_Red(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Lebanon(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Portugal(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Cuba(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Insurgents(Enum):
            USN_VRC_30 = "USN VRC-30"

        class SaudiArabia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class France(Enum):
            USN_VRC_30 = "USN VRC-30"

        class USA(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Honduras(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Qatar(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Russia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class United_Arab_Emirates(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Italian_Social_Republi(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Austria(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Bahrain(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Italy(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Chile(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Turkey(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Philippines(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Algeria(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Pakistan(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Malaysia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Indonesia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Iraq(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Germany(Enum):
            USN_VRC_30 = "USN VRC-30"

        class South_Africa(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Jordan(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Mexico(Enum):
            USN_VRC_30 = "USN VRC-30"

        class USAFAggressors(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Brazil(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Spain(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Belarus(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Canada(Enum):
            USN_VRC_30 = "USN VRC-30"

        class NorthKorea(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Ethiopia(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Japan(Enum):
            USN_VRC_30 = "USN VRC-30"

        class Thailand(Enum):
            USN_VRC_30 = "USN VRC-30"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class C5_Galaxy(PlaneType):
    id = "C5_Galaxy"
    group_size_max = 1
    height = 16.79
    width = 60.89
    length = 53.04
    fuel_max = 157768
    max_speed = 856.008
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    category = "Interceptor"  #{78EFB7A2-FD52-4b57-A6A6-3BF0E1D6555F}
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Georgia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Venezuela(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Australia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Israel(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Sudan(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Norway(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Romania(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Iran(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Ukraine(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Libya(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Belgium(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Slovakia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Greece(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class UK(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Third_Reich(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Hungary(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Abkhazia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Morocco(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class United_Nations_Peacekeepers(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Switzerland(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class SouthOssetia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Vietnam(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class China(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Yemen(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Kuwait(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Serbia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Oman(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class India(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Egypt(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class TheNetherlands(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Poland(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Syria(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Finland(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Kazakhstan(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Denmark(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Sweden(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Croatia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class CzechRepublic(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class GDR(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Yugoslavia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Bulgaria(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class SouthKorea(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Tunisia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Combined_Joint_Task_Forces_Red(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Lebanon(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Portugal(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Cuba(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Insurgents(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class SaudiArabia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class France(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class USA(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Honduras(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Qatar(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Russia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class United_Arab_Emirates(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Italian_Social_Republi(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Austria(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Bahrain(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Italy(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Chile(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Turkey(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Philippines(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Algeria(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Pakistan(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Malaysia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Indonesia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Iraq(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Germany(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class South_Africa(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Jordan(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Mexico(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class USAFAggressors(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Brazil(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Spain(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Belarus(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Canada(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class NorthKorea(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Ethiopia(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Japan(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

        class Thailand(Enum):
            Travis_AMC = "Travis AMC"
            Travis_AMC_static = "Travis AMC static"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport


class KC_10_Extender(PlaneType):
    id = "KC_10_Extender"
    group_size_max = 1
    height = 17.7
    width = 50.41
    length = 55.35
    fuel_max = 160200
    max_speed = 996.012
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    class Liveries:

        class USSR(Enum):
            Standard = "Standard"

        class Georgia(Enum):
            Standard = "Standard"

        class Venezuela(Enum):
            Standard = "Standard"

        class Australia(Enum):
            Standard = "Standard"

        class Israel(Enum):
            Standard = "Standard"

        class Combined_Joint_Task_Forces_Blue(Enum):
            Standard = "Standard"

        class Sudan(Enum):
            Standard = "Standard"

        class Norway(Enum):
            Standard = "Standard"

        class Romania(Enum):
            Standard = "Standard"

        class Iran(Enum):
            Standard = "Standard"

        class Ukraine(Enum):
            Standard = "Standard"

        class Libya(Enum):
            Standard = "Standard"

        class Belgium(Enum):
            Standard = "Standard"

        class Slovakia(Enum):
            Standard = "Standard"

        class Greece(Enum):
            Standard = "Standard"

        class UK(Enum):
            Standard = "Standard"

        class Third_Reich(Enum):
            Standard = "Standard"

        class Hungary(Enum):
            Standard = "Standard"

        class Abkhazia(Enum):
            Standard = "Standard"

        class Morocco(Enum):
            Standard = "Standard"

        class United_Nations_Peacekeepers(Enum):
            Standard = "Standard"

        class Switzerland(Enum):
            Standard = "Standard"

        class SouthOssetia(Enum):
            Standard = "Standard"

        class Vietnam(Enum):
            Standard = "Standard"

        class China(Enum):
            Standard = "Standard"

        class Yemen(Enum):
            Standard = "Standard"

        class Kuwait(Enum):
            Standard = "Standard"

        class Serbia(Enum):
            Standard = "Standard"

        class Oman(Enum):
            Standard = "Standard"

        class India(Enum):
            Standard = "Standard"

        class Egypt(Enum):
            Standard = "Standard"

        class TheNetherlands(Enum):
            Standard = "Standard"

        class Poland(Enum):
            Standard = "Standard"

        class Syria(Enum):
            Standard = "Standard"

        class Finland(Enum):
            Standard = "Standard"

        class Kazakhstan(Enum):
            Standard = "Standard"

        class Denmark(Enum):
            Standard = "Standard"

        class Sweden(Enum):
            Standard = "Standard"

        class Croatia(Enum):
            Standard = "Standard"

        class CzechRepublic(Enum):
            Standard = "Standard"

        class GDR(Enum):
            Standard = "Standard"

        class Yugoslavia(Enum):
            Standard = "Standard"

        class Bulgaria(Enum):
            Standard = "Standard"

        class SouthKorea(Enum):
            Standard = "Standard"

        class Tunisia(Enum):
            Standard = "Standard"

        class Combined_Joint_Task_Forces_Red(Enum):
            Standard = "Standard"

        class Lebanon(Enum):
            Standard = "Standard"

        class Portugal(Enum):
            Standard = "Standard"

        class Cuba(Enum):
            Standard = "Standard"

        class Insurgents(Enum):
            Standard = "Standard"

        class SaudiArabia(Enum):
            Standard = "Standard"

        class France(Enum):
            Standard = "Standard"

        class USA(Enum):
            Standard = "Standard"

        class Honduras(Enum):
            Standard = "Standard"

        class Qatar(Enum):
            Standard = "Standard"

        class Russia(Enum):
            Standard = "Standard"

        class United_Arab_Emirates(Enum):
            Standard = "Standard"

        class Italian_Social_Republi(Enum):
            Standard = "Standard"

        class Austria(Enum):
            Standard = "Standard"

        class Bahrain(Enum):
            Standard = "Standard"

        class Italy(Enum):
            Standard = "Standard"

        class Chile(Enum):
            Standard = "Standard"

        class Turkey(Enum):
            Standard = "Standard"

        class Philippines(Enum):
            Standard = "Standard"

        class Algeria(Enum):
            Standard = "Standard"

        class Pakistan(Enum):
            Standard = "Standard"

        class Malaysia(Enum):
            Standard = "Standard"

        class Indonesia(Enum):
            Standard = "Standard"

        class Iraq(Enum):
            Standard = "Standard"

        class Germany(Enum):
            Standard = "Standard"

        class South_Africa(Enum):
            Standard = "Standard"

        class Jordan(Enum):
            Standard = "Standard"

        class Mexico(Enum):
            Standard = "Standard"

        class USAFAggressors(Enum):
            Standard = "Standard"

        class Brazil(Enum):
            Standard = "Standard"

        class Spain(Enum):
            Standard = "Standard"

        class Belarus(Enum):
            Standard = "Standard"

        class Canada(Enum):
            Standard = "Standard"

        class NorthKorea(Enum):
            Standard = "Standard"

        class Ethiopia(Enum):
            Standard = "Standard"

        class Japan(Enum):
            Standard = "Standard"

        class Thailand(Enum):
            Standard = "Standard"

    pylons = {}

    tasks = [task.Transport, task.Refueling]
    task_default = task.Refueling


class KC_10_Extender_D(PlaneType):
    id = "KC_10_Extender_D"
    group_size_max = 1
    height = 17.7
    width = 50.41
    length = 55.35
    fuel_max = 154000
    max_speed = 804.996
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    tacan = True
    category = "Tankers"  #{8A302789-A55D-4897-B647-66493FA6826F}

    pylons = {}

    tasks = [task.Transport, task.Refueling]
    task_default = task.Refueling


class P3C_Orion(PlaneType):
    id = "P3C_Orion"
    group_size_max = 1
    height = 10.27
    width = 30.37
    length = 35.61
    fuel_max = 28350
    max_speed = 1479.6
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True
    radio_frequency = 127.5

    class Liveries:

        class USSR(Enum):
            USN_VP_11 = "USN VP-11"

        class Georgia(Enum):
            USN_VP_11 = "USN VP-11"

        class Venezuela(Enum):
            USN_VP_11 = "USN VP-11"

        class Australia(Enum):
            USN_VP_11 = "USN VP-11"

        class Israel(Enum):
            USN_VP_11 = "USN VP-11"

        class Combined_Joint_Task_Forces_Blue(Enum):
            USN_VP_11 = "USN VP-11"

        class Sudan(Enum):
            USN_VP_11 = "USN VP-11"

        class Norway(Enum):
            USN_VP_11 = "USN VP-11"

        class Romania(Enum):
            USN_VP_11 = "USN VP-11"

        class Iran(Enum):
            USN_VP_11 = "USN VP-11"

        class Ukraine(Enum):
            USN_VP_11 = "USN VP-11"

        class Libya(Enum):
            USN_VP_11 = "USN VP-11"

        class Belgium(Enum):
            USN_VP_11 = "USN VP-11"

        class Slovakia(Enum):
            USN_VP_11 = "USN VP-11"

        class Greece(Enum):
            USN_VP_11 = "USN VP-11"

        class UK(Enum):
            USN_VP_11 = "USN VP-11"

        class Third_Reich(Enum):
            USN_VP_11 = "USN VP-11"

        class Hungary(Enum):
            USN_VP_11 = "USN VP-11"

        class Abkhazia(Enum):
            USN_VP_11 = "USN VP-11"

        class Morocco(Enum):
            USN_VP_11 = "USN VP-11"

        class United_Nations_Peacekeepers(Enum):
            USN_VP_11 = "USN VP-11"

        class Switzerland(Enum):
            USN_VP_11 = "USN VP-11"

        class SouthOssetia(Enum):
            USN_VP_11 = "USN VP-11"

        class Vietnam(Enum):
            USN_VP_11 = "USN VP-11"

        class China(Enum):
            USN_VP_11 = "USN VP-11"

        class Yemen(Enum):
            USN_VP_11 = "USN VP-11"

        class Kuwait(Enum):
            USN_VP_11 = "USN VP-11"

        class Serbia(Enum):
            USN_VP_11 = "USN VP-11"

        class Oman(Enum):
            USN_VP_11 = "USN VP-11"

        class India(Enum):
            USN_VP_11 = "USN VP-11"

        class Egypt(Enum):
            USN_VP_11 = "USN VP-11"

        class TheNetherlands(Enum):
            USN_VP_11 = "USN VP-11"

        class Poland(Enum):
            USN_VP_11 = "USN VP-11"

        class Syria(Enum):
            USN_VP_11 = "USN VP-11"

        class Finland(Enum):
            USN_VP_11 = "USN VP-11"

        class Kazakhstan(Enum):
            USN_VP_11 = "USN VP-11"

        class Denmark(Enum):
            USN_VP_11 = "USN VP-11"

        class Sweden(Enum):
            USN_VP_11 = "USN VP-11"

        class Croatia(Enum):
            USN_VP_11 = "USN VP-11"

        class CzechRepublic(Enum):
            USN_VP_11 = "USN VP-11"

        class GDR(Enum):
            USN_VP_11 = "USN VP-11"

        class Yugoslavia(Enum):
            USN_VP_11 = "USN VP-11"

        class Bulgaria(Enum):
            USN_VP_11 = "USN VP-11"

        class SouthKorea(Enum):
            USN_VP_11 = "USN VP-11"

        class Tunisia(Enum):
            USN_VP_11 = "USN VP-11"

        class Combined_Joint_Task_Forces_Red(Enum):
            USN_VP_11 = "USN VP-11"

        class Lebanon(Enum):
            USN_VP_11 = "USN VP-11"

        class Portugal(Enum):
            USN_VP_11 = "USN VP-11"

        class Cuba(Enum):
            USN_VP_11 = "USN VP-11"

        class Insurgents(Enum):
            USN_VP_11 = "USN VP-11"

        class SaudiArabia(Enum):
            USN_VP_11 = "USN VP-11"

        class France(Enum):
            USN_VP_11 = "USN VP-11"

        class USA(Enum):
            USN_VP_11 = "USN VP-11"

        class Honduras(Enum):
            USN_VP_11 = "USN VP-11"

        class Qatar(Enum):
            USN_VP_11 = "USN VP-11"

        class Russia(Enum):
            USN_VP_11 = "USN VP-11"

        class United_Arab_Emirates(Enum):
            USN_VP_11 = "USN VP-11"

        class Italian_Social_Republi(Enum):
            USN_VP_11 = "USN VP-11"

        class Austria(Enum):
            USN_VP_11 = "USN VP-11"

        class Bahrain(Enum):
            USN_VP_11 = "USN VP-11"

        class Italy(Enum):
            USN_VP_11 = "USN VP-11"

        class Chile(Enum):
            USN_VP_11 = "USN VP-11"

        class Turkey(Enum):
            USN_VP_11 = "USN VP-11"

        class Philippines(Enum):
            USN_VP_11 = "USN VP-11"

        class Algeria(Enum):
            USN_VP_11 = "USN VP-11"

        class Pakistan(Enum):
            USN_VP_11 = "USN VP-11"

        class Malaysia(Enum):
            USN_VP_11 = "USN VP-11"

        class Indonesia(Enum):
            USN_VP_11 = "USN VP-11"

        class Iraq(Enum):
            USN_VP_11 = "USN VP-11"

        class Germany(Enum):
            USN_VP_11 = "USN VP-11"

        class South_Africa(Enum):
            USN_VP_11 = "USN VP-11"

        class Jordan(Enum):
            USN_VP_11 = "USN VP-11"

        class Mexico(Enum):
            USN_VP_11 = "USN VP-11"

        class USAFAggressors(Enum):
            USN_VP_11 = "USN VP-11"

        class Brazil(Enum):
            USN_VP_11 = "USN VP-11"

        class Spain(Enum):
            USN_VP_11 = "USN VP-11"

        class Belarus(Enum):
            USN_VP_11 = "USN VP-11"

        class Canada(Enum):
            USN_VP_11 = "USN VP-11"

        class NorthKorea(Enum):
            USN_VP_11 = "USN VP-11"

        class Ethiopia(Enum):
            USN_VP_11 = "USN VP-11"

        class Japan(Enum):
            USN_VP_11 = "USN VP-11"

        class Thailand(Enum):
            USN_VP_11 = "USN VP-11"

    class Pylon1:
        Smokewinder___red = (1, Weapons.Smokewinder___red)
        Smokewinder___green = (1, Weapons.Smokewinder___green)
        Smokewinder___blue = (1, Weapons.Smokewinder___blue)
        Smokewinder___white = (1, Weapons.Smokewinder___white)
        Smokewinder___yellow = (1, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (1, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU_115_LAU_127_AIM_9L = (1, Weapons.LAU_115_LAU_127_AIM_9L)
        Mk_82___500lb_GP_Bomb_LD = (1, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (1, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        AGM_84D_Harpoon_AShM = (1, Weapons.AGM_84D_Harpoon_AShM)

    class Pylon2:
        LAU_115_LAU_127_AIM_9L = (2, Weapons.LAU_115_LAU_127_AIM_9L)
        Mk_82___500lb_GP_Bomb_LD = (2, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (2, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (2, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        AGM_84D_Harpoon_AShM = (2, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (2, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (2, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (2, Weapons.LAU_117_AGM_65F)
        LAU_117_AGM_65G = (2, Weapons.LAU_117_AGM_65G)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (2, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)

    class Pylon3:
        Mk_82___500lb_GP_Bomb_LD = (3, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (3, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (3, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (3, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        AGM_84D_Harpoon_AShM = (3, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (3, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (3, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (3, Weapons.LAU_117_AGM_65F)
        LAU_117_AGM_65G = (3, Weapons.LAU_117_AGM_65G)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (3, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)

    class Pylon4:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (4, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (4, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon5:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (5, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (5, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon6:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (6, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (6, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (6, Weapons.Mk_83___1000lb_GP_Bomb_LD)

    class Pylon7:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (7, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (7, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (7, Weapons.Mk_83___1000lb_GP_Bomb_LD)

    class Pylon8:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (8, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (8, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (8, Weapons.Mk_83___1000lb_GP_Bomb_LD)

    class Pylon9:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (9, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (9, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_83___1000lb_GP_Bomb_LD = (9, Weapons.Mk_83___1000lb_GP_Bomb_LD)

    class Pylon10:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (10, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (10, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon11:
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (11, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        Mk_82___500lb_GP_Bomb_LD = (11, Weapons.Mk_82___500lb_GP_Bomb_LD)

    class Pylon12:
        Mk_82___500lb_GP_Bomb_LD = (12, Weapons.Mk_82___500lb_GP_Bomb_LD)
        BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD = (12, Weapons.BRU_42_with_3_x_Mk_82___500lb_GP_Bombs_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (12, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (12, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        AGM_84D_Harpoon_AShM = (12, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (12, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (12, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (12, Weapons.LAU_117_AGM_65F)
        LAU_117_AGM_65G = (12, Weapons.LAU_117_AGM_65G)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (12, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)

    class Pylon13:
        LAU_115_LAU_127_AIM_9L = (13, Weapons.LAU_115_LAU_127_AIM_9L)
        Mk_82___500lb_GP_Bomb_LD = (13, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (13, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets = (13, Weapons.MER2_with_2_x_Mk_20_Rockeye___490lbs_CBUs__247_x_HEAT_Bomblets)
        AGM_84D_Harpoon_AShM = (13, Weapons.AGM_84D_Harpoon_AShM)
        AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_ = (13, Weapons.AGM_84E_Harpoon_SLAM__Stand_Off_Land_Attack_Missile_)
        LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_ = (13, Weapons.LAU_117_with_AGM_65E___Maverick_E__Laser_ASM___Lg_Whd_)
        LAU_117_AGM_65F = (13, Weapons.LAU_117_AGM_65F)
        LAU_117_AGM_65G = (13, Weapons.LAU_117_AGM_65G)
        LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG = (13, Weapons.LAU_10_pod___4_x_127mm_ZUNI__UnGd_Rkts_Mk71__HE_FRAG)

    class Pylon14:
        Smokewinder___red = (14, Weapons.Smokewinder___red)
        Smokewinder___green = (14, Weapons.Smokewinder___green)
        Smokewinder___blue = (14, Weapons.Smokewinder___blue)
        Smokewinder___white = (14, Weapons.Smokewinder___white)
        Smokewinder___yellow = (14, Weapons.Smokewinder___yellow)
        AN_ASQ_T50_TCTS_Pod___ACMI_Pod = (14, Weapons.AN_ASQ_T50_TCTS_Pod___ACMI_Pod)
        LAU_115_LAU_127_AIM_9L = (14, Weapons.LAU_115_LAU_127_AIM_9L)
        Mk_82___500lb_GP_Bomb_LD = (14, Weapons.Mk_82___500lb_GP_Bomb_LD)
        Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets = (14, Weapons.Mk_20_Rockeye___490lbs_CBU__247_x_HEAT_Bomblets)
        AGM_84D_Harpoon_AShM = (14, Weapons.AGM_84D_Harpoon_AShM)

    pylons = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

    tasks = [task.Transport, task.GroundAttack, task.CAS, task.AFAC, task.RunwayAttack, task.AntishipStrike]
    task_default = task.AntishipStrike


class V22_Osprey(PlaneType):
    id = "V22_Osprey"
    group_size_max = 1
    height = 6.63
    width = 25.78
    length = 17.48
    fuel_max = 6103
    max_speed = 2649.996
    chaff = 120
    flare = 60
    charge_total = 240
    chaff_charge_size = 1
    flare_charge_size = 2
    eplrs = True

    class Liveries:

        class USSR(Enum):
            USAF = "USAF"

        class Georgia(Enum):
            USAF = "USAF"

        class Venezuela(Enum):
            USAF = "USAF"

        class Australia(Enum):
            USAF = "USAF"

        class Israel(Enum):
            USAF = "USAF"

        class Combined_Joint_Task_Forces_Blue(Enum):
            USAF = "USAF"

        class Sudan(Enum):
            USAF = "USAF"

        class Norway(Enum):
            USAF = "USAF"

        class Romania(Enum):
            USAF = "USAF"

        class Iran(Enum):
            USAF = "USAF"

        class Ukraine(Enum):
            USAF = "USAF"

        class Libya(Enum):
            USAF = "USAF"

        class Belgium(Enum):
            USAF = "USAF"

        class Slovakia(Enum):
            USAF = "USAF"

        class Greece(Enum):
            USAF = "USAF"

        class UK(Enum):
            USAF = "USAF"

        class Third_Reich(Enum):
            USAF = "USAF"

        class Hungary(Enum):
            USAF = "USAF"

        class Abkhazia(Enum):
            USAF = "USAF"

        class Morocco(Enum):
            USAF = "USAF"

        class United_Nations_Peacekeepers(Enum):
            USAF = "USAF"

        class Switzerland(Enum):
            USAF = "USAF"

        class SouthOssetia(Enum):
            USAF = "USAF"

        class Vietnam(Enum):
            USAF = "USAF"

        class China(Enum):
            USAF = "USAF"

        class Yemen(Enum):
            USAF = "USAF"

        class Kuwait(Enum):
            USAF = "USAF"

        class Serbia(Enum):
            USAF = "USAF"

        class Oman(Enum):
            USAF = "USAF"

        class India(Enum):
            USAF = "USAF"

        class Egypt(Enum):
            USAF = "USAF"

        class TheNetherlands(Enum):
            USAF = "USAF"

        class Poland(Enum):
            USAF = "USAF"

        class Syria(Enum):
            USAF = "USAF"

        class Finland(Enum):
            USAF = "USAF"

        class Kazakhstan(Enum):
            USAF = "USAF"

        class Denmark(Enum):
            USAF = "USAF"

        class Sweden(Enum):
            USAF = "USAF"

        class Croatia(Enum):
            USAF = "USAF"

        class CzechRepublic(Enum):
            USAF = "USAF"

        class GDR(Enum):
            USAF = "USAF"

        class Yugoslavia(Enum):
            USAF = "USAF"

        class Bulgaria(Enum):
            USAF = "USAF"

        class SouthKorea(Enum):
            USAF = "USAF"

        class Tunisia(Enum):
            USAF = "USAF"

        class Combined_Joint_Task_Forces_Red(Enum):
            USAF = "USAF"

        class Lebanon(Enum):
            USAF = "USAF"

        class Portugal(Enum):
            USAF = "USAF"

        class Cuba(Enum):
            USAF = "USAF"

        class Insurgents(Enum):
            USAF = "USAF"

        class SaudiArabia(Enum):
            USAF = "USAF"

        class France(Enum):
            USAF = "USAF"

        class USA(Enum):
            USAF = "USAF"

        class Honduras(Enum):
            USAF = "USAF"

        class Qatar(Enum):
            USAF = "USAF"

        class Russia(Enum):
            USAF = "USAF"

        class United_Arab_Emirates(Enum):
            USAF = "USAF"

        class Italian_Social_Republi(Enum):
            USAF = "USAF"

        class Austria(Enum):
            USAF = "USAF"

        class Bahrain(Enum):
            USAF = "USAF"

        class Italy(Enum):
            USAF = "USAF"

        class Chile(Enum):
            USAF = "USAF"

        class Turkey(Enum):
            USAF = "USAF"

        class Philippines(Enum):
            USAF = "USAF"

        class Algeria(Enum):
            USAF = "USAF"

        class Pakistan(Enum):
            USAF = "USAF"

        class Malaysia(Enum):
            USAF = "USAF"

        class Indonesia(Enum):
            USAF = "USAF"

        class Iraq(Enum):
            USAF = "USAF"

        class Germany(Enum):
            USAF = "USAF"

        class South_Africa(Enum):
            USAF = "USAF"

        class Jordan(Enum):
            USAF = "USAF"

        class Mexico(Enum):
            USAF = "USAF"

        class USAFAggressors(Enum):
            USAF = "USAF"

        class Brazil(Enum):
            USAF = "USAF"

        class Spain(Enum):
            USAF = "USAF"

        class Belarus(Enum):
            USAF = "USAF"

        class Canada(Enum):
            USAF = "USAF"

        class NorthKorea(Enum):
            USAF = "USAF"

        class Ethiopia(Enum):
            USAF = "USAF"

        class Japan(Enum):
            USAF = "USAF"

        class Thailand(Enum):
            USAF = "USAF"

    pylons = {}

    tasks = [task.Transport]
    task_default = task.Transport

