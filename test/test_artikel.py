import unittest
from cfg_initialization import cfg_true_or_false


class TestArtikel(unittest.TestCase):
    def test_artikel_01(self):
        """
        -> S-P-PEL ([A-N]-P-FPREP)
        (sang, artikel), (ratu, nomina), (pergi, verba),
        (ke, preposisi), (istana), (., td_akhir_kal)
        """
        kal = [
            "<artikel>",
            "<nomina>",
            "<verba>",
            "<preposisi>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_02(self):
        """
        -> S-P-O ([A-FNUM]-V-FN)
        (sri, artikel), (sultan, nomina), (hamengkubuwono, nomina),
        (x, numeralia), (menghadiri, verba), (acara, nomina),
        (gerebek, nomina), (suro, nomina), (., td_akhir_kal)
        """
        kal = [
            "<artikel>",
            "<nomina>",
            "<nomina>",
            "<numeralia>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_03(self):
        """
        -> S-P-O-PEL ([A-FNUM]-V-N-FPREP)
        (umat, artikel), (hindu, nomina), (memohon, verba),
        (keselamatan, nomina), (pada, preposisi),
        (hyang, artikel), (widhi, nomina), (., td_akhir_kal)
        """
        kal = [
            "<artikel>",
            "<nomina>",
            "<verba>",
            "<nomina>",
            "<preposisi>",
            "<artikel>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_yang_01(self):
        """
        -> S-P-O (F_KJ_YANG-V-FNUM)
        (yang, kj_sub_yang), (maha, adverbia), (esa, adjektiva),
        (mencintai, verba), (semua, numeralia), (manusia, nomina),
        (., td_akhir_kal)
        """
        kal = [
            "<kj_sub_yang>",
            "<adverbia>",
            "<adjektiva>",
            "<verba>",
            "<numeralia>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_yang_02(self):
        """
        -> P-S (V-F_KJ_YANG)
        (ada, verba), (yang, kj_sub_yang), (mengetuk, verba)
        (pintu, nomina), (., td_akhir_kal)
        """
        kal = [
            "<verba>",
            "<kj_sub_yang>",
            "<verba>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_per_01(self):
        """
        -> S-P (FNUM_FPREP-FADJ)
        (Dua, numeralia), (per, per), (lima, numeralia),
        (dari, preposisi), (populasi, nomina), (bumi, nomina),
        (telah, adverbia), (punah, adjektiva), (., td_akhir_kal)
        """
        kal = [
            "<numeralia>",
            "<per>",
            "<numeralia>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<adverbia>",
            "<adjektiva>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_per_02(self):
        """
        -> S-P-O (N-V-FN)
        (Itu, nomina), (dihitung, verba), (per, per),
        (orang,nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<per>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_per_03(self):
        """
        -> S-P-O (N-V-FNUM)
        (Gaji, nomina), (dibayarkan, verba), (dua, numeralia), (kali, nomina),
        (per, per), (bulan, nomina), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<numeralia>",
            "<nomina>",
            "<per>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_demi_01(self):
        """
        -> S-P (FNUM_PREP-V)
        (Satu, numeralia), (demi, demi), (satu, numeralia),
        (mereka, nomina), (keluar, verba), (., td_akhir_kal)
        """
        kal = [
            "<numeralia>",
            "<demi>",
            "<numeralia>",
            "<nomina>",
            "<verba>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_artikel_demi_02(self):
        """
        -> S-P (FNUM_PREP-V)
        (Mereka, nomina), (keluar, verba), (satu, numeralia),
        (demi, demi), (satu, numeralia), (., td_akhir_kal)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<numeralia>",
            "<demi>",
            "<numeralia>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))
