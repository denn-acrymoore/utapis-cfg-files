import unittest
from cfg_initialization import cfg_true_or_false


class TestSimbol(unittest.TestCase):
    def test_simbol_01(self):
        """
        -> S-P-PEL ([N-SIMBOL]-V-FPREP)
        (instagram, nomina), (@, simbol),
        (pergi, verba), (ke, preposisi),
        (kantor, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<simbol>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_simbol_02(self):
        """
        -> S-P-O (FN-V-[SIMBOL-NUM])
        (harga, nomina), (rumah, nomina), (itu, nomina),
        (adalah, verba), ($, simbol), (10, numeralia),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<simbol>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_simbol_03(self):
        """
        -> S-P-O (FN-V-[NUM-SIMBOL])
        (bunga, nomina), (rumah, nomina), (itu, nomina),
        (adalah, verba), (10, numeralia), (%, simbol),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<verba>",
            "<numeralia>",
            "<simbol>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_simbol_04(self):
        """
        -> S-P-PEL (N-V-FPREP_SIMBOL)
        (dia, nomina), (pergi, verba),
        (ke, preposisi), (^simbol, nomina),
        (pasar, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<simbol>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_simbol_05(self):
        """
        -> S-P (FN-FNUM)
        (ukuran, nomina), (rumah, nomina), (itu, nomina),
        (5, numeralia), (*, simbol), (5, numeralia),
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<simbol>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_simbol_06(self):
        """
        -> S-P (FN-V)
        (dia, nomina), (( atau [ atau { atau <, kurung_buka),
        (tono, nomina), () atau ] atau } atau >, kurung_tutup),
        (pergi, verba)
        (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<kurung_buka>",
            "<nomina>",
            "<kurung_tutup>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))
