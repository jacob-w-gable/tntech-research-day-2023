import string


class Cube:
    """
    Data representation of a cube

    Let "AB" represent a sticker position on the cube, where A
        is the side of the cube it's on, and B is the adjacent
        edge that it is near.

    For example, sticker position UB the sticker on the top of the cube (UP)
        and near the back of the cube (BACK).

    """

    EDGE_POSITIONS = {
        "UB": 0,
        "UR": 1,
        "UF": 2,
        "UL": 3,
        "FU": 4,
        "FR": 5,
        "FD": 6,
        "FL": 7,
        "BU": 8,
        "BR": 9,
        "BD": 10,
        "BL": 11,
        "LU": 12,
        "LF": 13,
        "LD": 14,
        "LB": 15,
        "RU": 16,
        "RB": 17,
        "RD": 18,
        "RF": 19,
        "DF": 20,
        "DR": 21,
        "DB": 22,
        "DL": 23,
    }

    EDGE_ADJACENTS = {
        "UB": "BU",
        "UR": "RU",
        "UF": "FU",
        "UL": "LU",
        "FU": "UF",
        "FR": "RF",
        "FD": "DF",
        "FL": "LF",
        "BU": "UB",
        "BR": "RB",
        "BD": "DB",
        "BL": "LB",
        "LU": "UL",
        "LF": "FL",
        "LD": "DL",
        "LB": "BL",
        "RU": "UR",
        "RB": "BR",
        "RD": "DR",
        "RF": "FR",
        "DF": "FD",
        "DR": "RD",
        "DB": "BD",
        "DL": "LD",
    }

    # Two ways to present each one
    CORNER_POSITIONS = {
        "UBL": 0,
        "ULB": 0,
        "UBR": 1,
        "URB": 1,
        "UFR": 2,
        "URF": 2,
        "UFL": 3,
        "ULF": 3,
        "FUL": 4,
        "FLU": 4,
        "FUR": 5,
        "FRU": 5,
        "FRD": 6,
        "FDR": 6,
        "FLD": 7,
        "FDL": 7,
        "BUL": 8,
        "BLU": 8,
        "BUR": 9,
        "BRU": 9,
        "BDR": 10,
        "BRD": 10,
        "BLD": 11,
        "BDL": 11,
        "LUB": 12,
        "LBU": 12,
        "LUF": 13,
        "LFU": 13,
        "LDB": 14,
        "LBD": 14,
        "LDF": 15,
        "LFD": 15,
        "RUF": 16,
        "RFU": 16,
        "RUB": 17,
        "RBU": 17,
        "RBD": 18,
        "RDB": 18,
        "RDF": 19,
        "RFD": 19,
        "DFL": 20,
        "DLF": 20,
        "DFR": 21,
        "DRF": 21,
        "DRB": 22,
        "DBR": 22,
        "DLB": 23,
        "DBL": 23,
    }

    CORNER_ADJACENT_RIGHT = {
        "UBL": "LUB",
        "ULB": "LUB",
        "UBR": "BUR",
        "URB": "BUR",
        "UFR": "RUF",
        "URF": "RUF",
        "UFL": "FUL",
        "ULF": "FUL",
        "FUL": "LUF",
        "FLU": "LUF",
        "FUR": "URF",
        "FRU": "URF",
        "FRD": "RFD",
        "FDR": "RFD",
        "FLD": "DFL",
        "FDL": "DFL",
        "BUL": "UBL",
        "BLU": "UBL",
        "BUR": "RUB",
        "BRU": "RUB",
        "BDR": "DBR",
        "BRD": "DBR",
        "BLD": "LBD",
        "BDL": "LBD",
        "LUB": "BUL",
        "LBU": "BUL",
        "LUF": "ULF",
        "LFU": "ULF",
        "LDB": "DLB",
        "LBD": "DLB",
        "LDF": "FDL",
        "LFD": "FDL",
        "RUF": "FUR",
        "RFU": "FUR",
        "RUB": "URB",
        "RBU": "URB",
        "RBD": "BDR",
        "RDB": "BDR",
        "RDF": "DFR",
        "RFD": "DFR",
        "DFL": "LDF",
        "DLF": "LDF",
        "DFR": "FDR",
        "DRF": "FDR",
        "DRB": "RDB",
        "DBR": "RDB",
        "DLB": "BLD",
        "DBL": "BLD",
    }

    CORNER_ADJACENT_LEFT = {
        "UBL": CORNER_ADJACENT_RIGHT["LUB"],
        "ULB": CORNER_ADJACENT_RIGHT["LUB"],
        "UBR": CORNER_ADJACENT_RIGHT["BUR"],
        "URB": CORNER_ADJACENT_RIGHT["BUR"],
        "UFR": CORNER_ADJACENT_RIGHT["RUF"],
        "URF": CORNER_ADJACENT_RIGHT["RUF"],
        "UFL": CORNER_ADJACENT_RIGHT["FUL"],
        "ULF": CORNER_ADJACENT_RIGHT["FUL"],
        "FUL": CORNER_ADJACENT_RIGHT["LUF"],
        "FLU": CORNER_ADJACENT_RIGHT["LUF"],
        "FUR": CORNER_ADJACENT_RIGHT["URF"],
        "FRU": CORNER_ADJACENT_RIGHT["URF"],
        "FRD": CORNER_ADJACENT_RIGHT["RFD"],
        "FDR": CORNER_ADJACENT_RIGHT["RFD"],
        "FLD": CORNER_ADJACENT_RIGHT["DFL"],
        "FDL": CORNER_ADJACENT_RIGHT["DFL"],
        "BUL": CORNER_ADJACENT_RIGHT["UBL"],
        "BLU": CORNER_ADJACENT_RIGHT["UBL"],
        "BUR": CORNER_ADJACENT_RIGHT["RUB"],
        "BRU": CORNER_ADJACENT_RIGHT["RUB"],
        "BDR": CORNER_ADJACENT_RIGHT["DBR"],
        "BRD": CORNER_ADJACENT_RIGHT["DBR"],
        "BLD": CORNER_ADJACENT_RIGHT["LBD"],
        "BDL": CORNER_ADJACENT_RIGHT["LBD"],
        "LUB": CORNER_ADJACENT_RIGHT["BUL"],
        "LBU": CORNER_ADJACENT_RIGHT["BUL"],
        "LUF": CORNER_ADJACENT_RIGHT["ULF"],
        "LFU": CORNER_ADJACENT_RIGHT["ULF"],
        "LDB": CORNER_ADJACENT_RIGHT["DLB"],
        "LBD": CORNER_ADJACENT_RIGHT["DLB"],
        "LDF": CORNER_ADJACENT_RIGHT["FDL"],
        "LFD": CORNER_ADJACENT_RIGHT["FDL"],
        "RUF": CORNER_ADJACENT_RIGHT["FUR"],
        "RFU": CORNER_ADJACENT_RIGHT["FUR"],
        "RUB": CORNER_ADJACENT_RIGHT["URB"],
        "RBU": CORNER_ADJACENT_RIGHT["URB"],
        "RBD": CORNER_ADJACENT_RIGHT["BDR"],
        "RDB": CORNER_ADJACENT_RIGHT["BDR"],
        "RDF": CORNER_ADJACENT_RIGHT["DFR"],
        "RFD": CORNER_ADJACENT_RIGHT["DFR"],
        "DFL": CORNER_ADJACENT_RIGHT["LDF"],
        "DLF": CORNER_ADJACENT_RIGHT["LDF"],
        "DFR": CORNER_ADJACENT_RIGHT["FDR"],
        "DRF": CORNER_ADJACENT_RIGHT["FDR"],
        "DRB": CORNER_ADJACENT_RIGHT["RDB"],
        "DBR": CORNER_ADJACENT_RIGHT["RDB"],
        "DLB": CORNER_ADJACENT_RIGHT["BLD"],
        "DBL": CORNER_ADJACENT_RIGHT["BLD"],
    }

    COLOR_MAP = {
        "U": "\U00002B1C",
        "D": "\U0001F7E8",
        "L": "\U0001F7E7",
        "R": "\U0001F7E5",
        "F": "\U0001F7E9",
        "B": "\U0001F7E6",
    }

    def __init__(self):
        self.instance_edges = {
            "UR": Cube.EDGE_POSITIONS["UR"],
            "UF": Cube.EDGE_POSITIONS["UF"],
            "UB": Cube.EDGE_POSITIONS["UB"],
            "UL": Cube.EDGE_POSITIONS["UL"],
            "FU": Cube.EDGE_POSITIONS["FU"],
            "FR": Cube.EDGE_POSITIONS["FR"],
            "FD": Cube.EDGE_POSITIONS["FD"],
            "FL": Cube.EDGE_POSITIONS["FL"],
            "BU": Cube.EDGE_POSITIONS["BU"],
            "BR": Cube.EDGE_POSITIONS["BR"],
            "BD": Cube.EDGE_POSITIONS["BD"],
            "BL": Cube.EDGE_POSITIONS["BL"],
            "LU": Cube.EDGE_POSITIONS["LU"],
            "LF": Cube.EDGE_POSITIONS["LF"],
            "LD": Cube.EDGE_POSITIONS["LD"],
            "LB": Cube.EDGE_POSITIONS["LB"],
            "RU": Cube.EDGE_POSITIONS["RU"],
            "RB": Cube.EDGE_POSITIONS["RB"],
            "RD": Cube.EDGE_POSITIONS["RD"],
            "RF": Cube.EDGE_POSITIONS["RF"],
            "DF": Cube.EDGE_POSITIONS["DF"],
            "DR": Cube.EDGE_POSITIONS["DR"],
            "DB": Cube.EDGE_POSITIONS["DB"],
            "DL": Cube.EDGE_POSITIONS["DL"],
        }

        self.instance_corners = {
            "UBL": Cube.CORNER_POSITIONS["UBL"],
            "UBR": Cube.CORNER_POSITIONS["UBR"],
            "UFR": Cube.CORNER_POSITIONS["UFR"],
            "UFL": Cube.CORNER_POSITIONS["UFL"],
            "FUL": Cube.CORNER_POSITIONS["FUL"],
            "FUR": Cube.CORNER_POSITIONS["FUR"],
            "FRD": Cube.CORNER_POSITIONS["FRD"],
            "FLD": Cube.CORNER_POSITIONS["FLD"],
            "BUL": Cube.CORNER_POSITIONS["BUL"],
            "BUR": Cube.CORNER_POSITIONS["BUR"],
            "BDR": Cube.CORNER_POSITIONS["BDR"],
            "BLD": Cube.CORNER_POSITIONS["BLD"],
            "LUB": Cube.CORNER_POSITIONS["LUB"],
            "LUF": Cube.CORNER_POSITIONS["LUF"],
            "LDB": Cube.CORNER_POSITIONS["LDB"],
            "LDF": Cube.CORNER_POSITIONS["LDF"],
            "RUF": Cube.CORNER_POSITIONS["RUF"],
            "RUB": Cube.CORNER_POSITIONS["RUB"],
            "RBD": Cube.CORNER_POSITIONS["RBD"],
            "RDF": Cube.CORNER_POSITIONS["RDF"],
            "DFL": Cube.CORNER_POSITIONS["DFL"],
            "DFR": Cube.CORNER_POSITIONS["DFR"],
            "DRB": Cube.CORNER_POSITIONS["DRB"],
            "DLB": Cube.CORNER_POSITIONS["DLB"],
        }

    def get_color(self, sticker: string):
        return Cube.COLOR_MAP[sticker[0]]

    def validate_corner(self, corner: string):
        if corner == "ULB":
            return "UBL"
        if corner == "URB":
            return "UBR"
        if corner == "URF":
            return "UFR"
        if corner == "ULF":
            return "UFL"
        if corner == "FLU":
            return "FUL"
        if corner == "FRU":
            return "FUR"
        if corner == "FDR":
            return "FRD"
        if corner == "FDL":
            return "FLD"
        if corner == "BLU":
            return "BUL"
        if corner == "BRU":
            return "BUR"
        if corner == "BRD":
            return "BDR"
        if corner == "BDL":
            return "BLD"
        if corner == "LBU":
            return "LUB"
        if corner == "LRU":
            return "LUR"
        if corner == "LBD":
            return "LDB"
        if corner == "LFD":
            return "LDF"
        if corner == "RFU":
            return "RUF"
        if corner == "RBU":
            return "RUB"
        if corner == "RDB":
            return "RBD"
        if corner == "RFD":
            return "RDF"
        if corner == "DLF":
            return "DFL"
        if corner == "DRF":
            return "DFR"
        if corner == "DBR":
            return "DRB"
        if corner == "DBL":
            return "DLB"

        return corner

    def rotate_edges(self, edge_1: string, edge_2: string, edge_3: string, edge_4: string):
        """
        edges are strings

        edge_1 goes to edge_2, edge_2 goes to edge_3, 
        edge_3 goes to edge_4, and edge_4 goes to edge_1
        """
        edge_1_adj = Cube.EDGE_ADJACENTS[edge_1]
        edge_2_adj = Cube.EDGE_ADJACENTS[edge_2]
        edge_3_adj = Cube.EDGE_ADJACENTS[edge_3]
        edge_4_adj = Cube.EDGE_ADJACENTS[edge_4]

        temp = self.instance_edges[edge_4]
        self.instance_edges[edge_4] = self.instance_edges[edge_3]
        self.instance_edges[edge_3] = self.instance_edges[edge_2]
        self.instance_edges[edge_2] = self.instance_edges[edge_1]
        self.instance_edges[edge_1] = temp

        temp = self.instance_edges[edge_4_adj]
        self.instance_edges[edge_4_adj] = self.instance_edges[edge_3_adj]
        self.instance_edges[edge_3_adj] = self.instance_edges[edge_2_adj]
        self.instance_edges[edge_2_adj] = self.instance_edges[edge_1_adj]
        self.instance_edges[edge_1_adj] = temp

    def swap_edges(self, edge_1: string, edge_2: string):
        edge_1_adj = Cube.EDGE_ADJACENTS[edge_1]
        edge_2_adj = Cube.EDGE_ADJACENTS[edge_2]

        temp = self.instance_edges[edge_2]
        self.instance_edges[edge_2] = self.instance_edges[edge_1]
        self.instance_edges[edge_1] = temp

        temp = self.instance_edges[edge_2_adj]
        self.instance_edges[edge_2_adj] = self.instance_edges[edge_1_adj]
        self.instance_edges[edge_1_adj] = temp

    def rotate_corners(self, corner_1: string, corner_2: string, corner_3: string, corner_4: string):
        """
        corners are strings

        corner_1 goes to corner_2, corner_2 goes to corner_3, 
        corner_3 goes to corner_4, and corner_4 goes to corner_1
        """

        corner_1 = self.validate_corner(corner_1)
        corner_2 = self.validate_corner(corner_2)
        corner_3 = self.validate_corner(corner_3)
        corner_4 = self.validate_corner(corner_4)

        corner_1_adj_right = self.validate_corner(
            Cube.CORNER_ADJACENT_RIGHT[corner_1])
        corner_2_adj_right = self.validate_corner(
            Cube.CORNER_ADJACENT_RIGHT[corner_2])
        corner_3_adj_right = self.validate_corner(
            Cube.CORNER_ADJACENT_RIGHT[corner_3])
        corner_4_adj_right = self.validate_corner(
            Cube.CORNER_ADJACENT_RIGHT[corner_4])

        corner_1_adj_left = self.validate_corner(
            Cube.CORNER_ADJACENT_LEFT[corner_1])
        corner_2_adj_left = self.validate_corner(
            Cube.CORNER_ADJACENT_LEFT[corner_2])
        corner_3_adj_left = self.validate_corner(
            Cube.CORNER_ADJACENT_LEFT[corner_3])
        corner_4_adj_left = self.validate_corner(
            Cube.CORNER_ADJACENT_LEFT[corner_4])

        temp = self.instance_corners[corner_4]
        self.instance_corners[corner_4] = self.instance_corners[corner_3]
        self.instance_corners[corner_3] = self.instance_corners[corner_2]
        self.instance_corners[corner_2] = self.instance_corners[corner_1]
        self.instance_corners[corner_1] = temp

        temp = self.instance_corners[corner_4_adj_right]
        self.instance_corners[corner_4_adj_right] = self.instance_corners[corner_3_adj_right]
        self.instance_corners[corner_3_adj_right] = self.instance_corners[corner_2_adj_right]
        self.instance_corners[corner_2_adj_right] = self.instance_corners[corner_1_adj_right]
        self.instance_corners[corner_1_adj_right] = temp

        temp = self.instance_corners[corner_4_adj_left]
        self.instance_corners[corner_4_adj_left] = self.instance_corners[corner_3_adj_left]
        self.instance_corners[corner_3_adj_left] = self.instance_corners[corner_2_adj_left]
        self.instance_corners[corner_2_adj_left] = self.instance_corners[corner_1_adj_left]
        self.instance_corners[corner_1_adj_left] = temp

    def swap_corners(self, corner_1: string, corner_2: string):
        corner_1 = self.validate_corner(corner_1)
        corner_2 = self.validate_corner(corner_2)

        corner_1_adj_right = self.validate_corner(
            Cube.CORNER_ADJACENT_RIGHT[corner_1])
        corner_2_adj_right = self.validate_corner(
            Cube.CORNER_ADJACENT_RIGHT[corner_2])

        corner_1_adj_left = self.validate_corner(
            Cube.CORNER_ADJACENT_LEFT[corner_1])
        corner_2_adj_left = self.validate_corner(
            Cube.CORNER_ADJACENT_LEFT[corner_2])

        temp = self.instance_corners[corner_2]
        self.instance_corners[corner_2] = self.instance_corners[corner_1]
        self.instance_corners[corner_1] = temp

        temp = self.instance_corners[corner_2_adj_right]
        self.instance_corners[corner_2_adj_right] = self.instance_corners[corner_1_adj_right]
        self.instance_corners[corner_1_adj_right] = temp

        temp = self.instance_corners[corner_2_adj_left]
        self.instance_corners[corner_2_adj_left] = self.instance_corners[corner_1_adj_left]
        self.instance_corners[corner_1_adj_left] = temp

    def rotate_R(self):
        self.rotate_edges("RU", "RB", "RD", "RF")
        self.rotate_corners("RUF", "RUB", "RDB", "RDF")

    def rotate_Ri(self):
        self.rotate_edges("RF", "RD", "RB", "RU")
        self.rotate_corners("RDF", "RDB", "RUB", "RUF")

    def rotate_R2(self):
        self.swap_edges("RU", "RD")
        self.swap_edges("RF", "RB")
        self.swap_corners("RUF", "RBD")
        self.swap_corners("RUB", "RFD")

    def rotate_L(self):
        self.rotate_edges("LU", "LF", "LD", "LB")
        self.rotate_corners("LUF", "LDF", "LDB", "LUB")

    def rotate_Li(self):
        self.rotate_edges("LB", "LD", "LF", "LU")
        self.rotate_corners("LUB", "LDB", "LDF", "LUF")

    def rotate_L2(self):
        self.swap_edges("LU", "LD")
        self.swap_edges("LF", "LB")
        self.swap_corners("LUF", "LBD")
        self.swap_corners("LUB", "LFD")

    def rotate_F(self):
        self.rotate_edges("FU", "FR", "FD", "FL")
        self.rotate_corners("FUL", "FUR", "FDR", "FDL")

    def rotate_Fi(self):
        self.rotate_edges("FL", "FD", "FR", "FU")
        self.rotate_corners("FDL", "FDR", "FUR", "FUL")

    def rotate_F2(self):
        self.swap_edges("FU", "FD")
        self.swap_edges("FL", "FR")
        self.swap_corners("FUL", "FDR")
        self.swap_corners("FUR", "FDL")

    def rotate_B(self):
        self.rotate_edges("BL", "BD", "BR", "BU")
        self.rotate_corners("BDL", "BDR", "BUR", "BUL")

    def rotate_Bi(self):
        self.rotate_edges("BU", "BR", "BD", "BL")
        self.rotate_corners("BUL", "BUR", "BDR", "BDL")

    def rotate_B2(self):
        self.swap_edges("BU", "BD")
        self.swap_edges("BL", "BR")
        self.swap_corners("BUL", "BDR")
        self.swap_corners("BUR", "BDL")

    def rotate_U(self):
        self.rotate_edges("UB", "UR", "UF", "UL")
        self.rotate_corners("UBL", "UBR", "UFR", "UFL")

    def rotate_Ui(self):
        self.rotate_edges("UL", "UF", "UR", "UB")
        self.rotate_corners("UFL", "UFR", "UBR", "UBL")

    def rotate_U2(self):
        self.swap_edges("UB", "UF")
        self.swap_edges("UL", "UR")
        self.swap_corners("UBL", "UFR")
        self.swap_corners("UBR", "UFL")

    def rotate_D(self):
        self.rotate_edges("DL", "DF", "DR", "DB")
        self.rotate_corners("DFL", "DFR", "DBR", "DBL")

    def rotate_Di(self):
        self.rotate_edges("DB", "DR", "DF", "DL")
        self.rotate_corners("DBL", "DBR", "DFR", "DFL")

    def rotate_D2(self):
        self.swap_edges("DB", "DF")
        self.swap_edges("DL", "DR")
        self.swap_corners("DBL", "DFR")
        self.swap_corners("DBR", "DFL")

    def scramble(self, scramble: string):
        turns = scramble.split(" ")
        for turn in turns:
            if turn == "R":
                self.rotate_R()
            if turn == "R'":
                self.rotate_Ri()
            if turn == "R2":
                self.rotate_R2()
            if turn == "L":
                self.rotate_L()
            if turn == "L'":
                self.rotate_Li()
            if turn == "L2":
                self.rotate_L2()
            if turn == "F":
                self.rotate_F()
            if turn == "F'":
                self.rotate_Fi()
            if turn == "F2":
                self.rotate_F2()
            if turn == "B":
                self.rotate_B()
            if turn == "B'":
                self.rotate_Bi()
            if turn == "B2":
                self.rotate_B2()
            if turn == "U":
                self.rotate_U()
            if turn == "U'":
                self.rotate_Ui()
            if turn == "U2":
                self.rotate_U2()
            if turn == "D":
                self.rotate_D()
            if turn == "D'":
                self.rotate_Di()
            if turn == "D2":
                self.rotate_D2()

    def get_position_color(self, position: string):
        """
        position: string  # e.g., "UBL"
        """
        if len(position) == 2:
            sticker_id = self.instance_edges[position]
            sticker_source = ""
            for sticker in Cube.EDGE_POSITIONS.keys():
                if sticker_id == Cube.EDGE_POSITIONS[sticker]:
                    sticker_source = sticker
                    break

            return self.get_color(sticker_source)

        else:
            position = self.validate_corner(position)
            sticker_id = self.instance_corners[position]
            sticker_source = ""
            for sticker in Cube.CORNER_POSITIONS.keys():
                if sticker_id == Cube.CORNER_POSITIONS[sticker]:
                    sticker_source = sticker
                    break

            return self.get_color(sticker_source)

    def compatbile_print(self):
        """
        Same as print, but without emojis
        """

        old_map = Cube.COLOR_MAP

        Cube.COLOR_MAP = {
            "U": "W",
            "D": "Y",
            "L": "O",
            "R": "R",
            "F": "G",
            "B": "B",
        }

        A = self.get_position_color("UBL")
        B = self.get_position_color("UB")
        C = self.get_position_color("UBR")

        D = self.get_position_color("UL")
        E = self.get_color("U")
        F = self.get_position_color("UR")

        G = self.get_position_color("UFL")
        H = self.get_position_color("UF")
        I = self.get_position_color("UFR")

        J = self.get_position_color("LUB")
        K = self.get_position_color("LU")
        L = self.get_position_color("LUF")
        M = self.get_position_color("FUL")
        N = self.get_position_color("FU")
        O = self.get_position_color("FUR")
        P = self.get_position_color("RUF")
        Q = self.get_position_color("RU")
        R = self.get_position_color("RUB")
        S = self.get_position_color("BUR")
        T = self.get_position_color("BU")
        U = self.get_position_color("BUL")

        V = self.get_position_color("LB")
        W = self.get_color("L")
        X = self.get_position_color("LF")
        Y = self.get_position_color("FL")
        Z = self.get_color("F")
        AA = self.get_position_color("FR")
        BB = self.get_position_color("RF")
        CC = self.get_color("R")
        DD = self.get_position_color("RB")
        EE = self.get_position_color("BR")
        FF = self.get_color("B")
        GG = self.get_position_color("BL")

        HH = self.get_position_color("LDB")
        II = self.get_position_color("LD")
        JJ = self.get_position_color("LDF")
        KK = self.get_position_color("FDL")
        LL = self.get_position_color("FD")
        MM = self.get_position_color("FDR")
        NN = self.get_position_color("RDF")
        OO = self.get_position_color("RD")
        PP = self.get_position_color("RDB")
        QQ = self.get_position_color("BDR")
        RR = self.get_position_color("BD")
        SS = self.get_position_color("BDL")

        TT = self.get_position_color("DFL")
        UU = self.get_position_color("DF")
        VV = self.get_position_color("DFR")
        WW = self.get_position_color("DL")
        XX = self.get_color("D")
        YY = self.get_position_color("DR")
        ZZ = self.get_position_color("DBL")
        AAA = self.get_position_color("DB")
        BBB = self.get_position_color("DBR")

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'          ___________')
        print(f'          |  {A} {B} {C}  |')
        print(f'          |  {D} {E} {F}  |')
        print(f'          |  {G} {H} {I}  |')
        print(f'__________|_________|____________________')
        print(f'|  {J} {K} {L}  |  {M} {N} {O}  |  {P} {Q} {R}  |  {S} {T} {U}  |')
        print(
            f'|  {V} {W} {X}  |  {Y} {Z} {AA}  |  {BB} {CC} {DD}  |  {EE} {FF} {GG}  |')
        print(
            f'|  {HH} {II} {JJ}  |  {KK} {LL} {MM}  |  {NN} {OO} {PP}  |  {QQ} {RR} {SS}  |')
        print(f'|_________|_________|_________|_________|')
        print(f'          |  {TT} {UU} {VV}  |')
        print(f'          |  {WW} {XX} {YY}  |')
        print(f'          |  {ZZ} {AAA} {BBB}  |')
        print(f'          |_________|')
        print(f'')
        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        Cube.COLOR_MAP = old_map

    def print(self):

        A = self.get_position_color("UBL")
        B = self.get_position_color("UB")
        C = self.get_position_color("UBR")

        D = self.get_position_color("UL")
        E = self.get_color("U")
        F = self.get_position_color("UR")

        G = self.get_position_color("UFL")
        H = self.get_position_color("UF")
        I = self.get_position_color("UFR")

        J = self.get_position_color("LUB")
        K = self.get_position_color("LU")
        L = self.get_position_color("LUF")
        M = self.get_position_color("FUL")
        N = self.get_position_color("FU")
        O = self.get_position_color("FUR")
        P = self.get_position_color("RUF")
        Q = self.get_position_color("RU")
        R = self.get_position_color("RUB")
        S = self.get_position_color("BUR")
        T = self.get_position_color("BU")
        U = self.get_position_color("BUL")

        V = self.get_position_color("LB")
        W = self.get_color("L")
        X = self.get_position_color("LF")
        Y = self.get_position_color("FL")
        Z = self.get_color("F")
        AA = self.get_position_color("FR")
        BB = self.get_position_color("RF")
        CC = self.get_color("R")
        DD = self.get_position_color("RB")
        EE = self.get_position_color("BR")
        FF = self.get_color("B")
        GG = self.get_position_color("BL")

        HH = self.get_position_color("LDB")
        II = self.get_position_color("LD")
        JJ = self.get_position_color("LDF")
        KK = self.get_position_color("FDL")
        LL = self.get_position_color("FD")
        MM = self.get_position_color("FDR")
        NN = self.get_position_color("RDF")
        OO = self.get_position_color("RD")
        PP = self.get_position_color("RDB")
        QQ = self.get_position_color("BDR")
        RR = self.get_position_color("BD")
        SS = self.get_position_color("BDL")

        TT = self.get_position_color("DFL")
        UU = self.get_position_color("DF")
        VV = self.get_position_color("DFR")
        WW = self.get_position_color("DL")
        XX = self.get_color("D")
        YY = self.get_position_color("DR")
        ZZ = self.get_position_color("DBL")
        AAA = self.get_position_color("DB")
        BBB = self.get_position_color("DBR")

        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f'')
        print(f'       {A}{B}{C}')
        print(f'       {D}{E}{F}')
        print(f'       {G}{H}{I}')
        print(f'')
        print(f'{J}{K}{L} {M}{N}{O} {P}{Q}{R} {S}{T}{U}')
        print(
            f'{V}{W}{X} {Y}{Z}{AA} {BB}{CC}{DD} {EE}{FF}{GG}')
        print(
            f'{HH}{II}{JJ} {KK}{LL}{MM} {NN}{OO}{PP} {QQ}{RR}{SS}')
        print(f'')
        print(f'       {TT}{UU}{VV}')
        print(f'       {WW}{XX}{YY}')
        print(f'       {ZZ}{AAA}{BBB}')
        print(f'')
        print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def make_features(self):
        """
        The features will be represented in an array of 1's an 0's

        There are 20 different pieces, each of which can be in 24 different positions.

        Each piece will be represented by an array of 1's and 0's of length 24. That
        array represents the location of the piece.
        """

        edges = ["UB", "UR", "UF", "UL", "FL", "FR",
                 "BL", "BR", "DB", "DR", "DF", "DL"]

        corners = ["UBL", "UBR", "UFR", "UFL", "DBL", "DBR", "DFR", "DFL"]
        for i, corner in enumerate(corners):
            corners[i] = self.validate_corner(corner)

        feature_array = []

        for edge in edges:
            edge_id = Cube.EDGE_POSITIONS[edge]
            for instance_edge in self.instance_edges.keys():
                if self.instance_edges[instance_edge] == edge_id:
                    edge_feature_array = [0]*24
                    edge_feature_array[Cube.EDGE_POSITIONS[instance_edge]] = 1
                    feature_array.extend(edge_feature_array)
                    break

        for corner in corners:
            corner_id = Cube.CORNER_POSITIONS[corner]
            for instance_corner in self.instance_corners.keys():
                if self.instance_corners[instance_corner] == corner_id:
                    corner_feature_array = [0]*24
                    corner_feature_array[Cube.CORNER_POSITIONS[instance_corner]] = 1
                    feature_array.extend(corner_feature_array)
                    break

        return feature_array


if __name__ == '__main__':
    cube = Cube()

    cube.print()

    scramble = "D2 L2 B2 D F2 D2 U' R2 F2 B D2 R D2 F' L R F U' B'"

    print(scramble)
    cube.scramble(scramble)

    cube.print()

    y = [0]*19
    y[len(scramble.split(" "))-1] = 1

    print("")
    print("X = ", cube.make_features())
    print("")
    print("y = ", y)
    print("")
