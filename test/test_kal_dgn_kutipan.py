import unittest
from cfg_initialization import cfg_true_or_false


class TestKalKutipan(unittest.TestCase):
    def test_hanya_kutipan_01(self):
        """
        -> Hanya kutipan
        (", kutip_awal), (., td_akhir_kal), (", kutip_akhir)
        """
        kal = [
            "<kutip_awal>",
            "<td_akhir_kal>",
            "<kutip_akhir>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kutipan_depan_01(self):
        """
        -> KUTIPAN-P-S (KUTIPAN-V-FN)
        (", kutip_awal), (,, td_koma), (", kutip_akhir), (ujar, verba),
        (para, artikel), (masyarakat, nomina), (., td_akhir_kal)
        """
        kal = [
            "<kutip_awal>",
            "<td_koma>",
            "<kutip_akhir>",
            "<verba>",
            "<artikel>",
            "<nomina>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kutipan_depan_02(self):
        """
        -> KUTIPAN-P-S-PEL-F_KURUNG (KUTIPAN-V-FN-FPREP-F_KURUNG)
        (", kutip_awal), (,, koma), (", kutip_akhir), (kata, verba), (Kabid, nomina),
        (Litbang, nomina), (PP, nomina), (The, nomina), (Jakmania, nomina),
        (,, td_koma), (Afrizal, nomina), (Kasriyanto, nomina), (kepada, preposisi),
        (tribunnews.com, nomina), (,, td_koma), (Jumat, nomina), ('(', kurung buka),
        (26/11/2021, numeralia), (')', kurung tutup), (., td_akhir_kal)
        """
        kal = [
            "<kutip_awal>",
            "<td_koma>",
            "<kutip_akhir>",
            "<verba>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<nomina>",
            "<preposisi>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<kurung_buka>",
            "<numeralia>",
            "<kurung_tutup>",
            "<td_akhir_kal>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kutipan_belakang_01(self):
        """
        -> P-S-KUTIPAN (V-FNUM-KUTIPAN)
        (Menurut, verba), (UUD, nomina), (1945, numeralia), (,, td_koma),
        (", kutip_awal), (., td_akhir_kal), (", kutip_akhir)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<td_koma>",
            "<kutip_awal>",
            "<td_akhir_kal>",
            "<kutip_akhir>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_kutipan_belakang_02(self):
        """
        -> Kutipan belakang 02
        (Ia, nomina), (mengungkapkan, verba), (,, td_koma), (dari, preposisi),
        (dalam, nomina), (lubuk, nomina), (hatinya, nomina), (,, td_koma),
        (perasaan, nomina), (yang, kj_sub_yang), (dimilikinya, verba),
        (,, td_koma), (", kutip_awal), (., td_akhir_kal), (", kutip_akhir)
        """
        kal = [
            "<nomina>",
            "<verba>",
            "<td_koma>",
            "<preposisi>",
            "<nomina>",
            "<nomina>",
            "<nomina>",
            "<td_koma>",
            "<nomina>",
            "<kj_sub_yang>",
            "<verba>",
            "<td_koma>",
            "<kutip_awal>",
            "<td_akhir_kal>",
            "<kutip_akhir>",
        ]
        self.assertTrue(cfg_true_or_false(kal))

    def test_salah_kutipan_01(self):
        """
        -> Tes: Kutipan tidak mengandung tanda akhir kal.
        (", kutip_awal), (,, td_koma), (", kutip_akhir)
        """
        kal = [
            "<kutip_awal>",
            "<td_koma>",
            "<kutip_akhir>",
        ]
        self.assertFalse(cfg_true_or_false(kal))

    def test_salah_kutipan_02(self):
        """
        -> Tes: Tanda akhir kalimat di luar kutipan.
        (", kutip_awal), (", kutip_akhir), (., td_akhir_kal)
        """
        kal = [
            "<kutip_awal>",
            "<kutip_akhir>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))

    def test_salah_kutipan_03(self):
        """
        -> Tes: Kutipan akhir kalimat tidak dipisahkan dengan koma.
        (Menurut, verba), (UUD, nomina), (1945, numeralia),
        (", kutip_awal), (., td_akhir_kal), (", kutip_akhir)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<kutip_awal>",
            "<td_akhir_kal>",
            "<kutip_akhir>",
        ]
        self.assertFalse(cfg_true_or_false(kal))

    def test_salah_kutipan_04(self):
        """
        -> Tes: Tanda akhir kalimat di luar kutipan akhir kalimat.
        (Menurut, verba), (UUD, nomina), (1945, numeralia), (,, td_koma),
        (", kutip_awal), (", kutip_akhir), (., td_akhir_kal)
        """
        kal = [
            "<verba>",
            "<nomina>",
            "<numeralia>",
            "<td_koma>",
            "<kutip_awal>",
            "<kutip_akhir>",
            "<td_akhir_kal>",
        ]
        self.assertFalse(cfg_true_or_false(kal))
