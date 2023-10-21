import sys
import json
import mysql.connector
import pdfplumber
from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1
from google.cloud.automl_v1.proto import service_pb2
import re, os
import collections
import datetime
from google.cloud import storage
import math
import traceback
import logging


def inline_text_payload(file_path):
    with open(file_path, 'rb') as ff:
        content = ff.read()
    return {'text_snippet': {'content': content, 'mime_type': 'text/plain'}}


def pdf_payload(file_path):
    return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path]}}}}


def get_prediction(file_path, model_name):
    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(client_options=options)

    # payload = inline_text_payload(file_path)
    # Uncomment the following line (and comment the above line) if want to predict on PDFs.
    payload = pdf_payload(file_path)

    params = {}
    request = prediction_client.predict(model_name, payload, params)
    return request  # waits until request is returned


def years_fun(lines):
    # Assuming Sorted False
    IncomeStatementdict = [
        ".*Consolidated.*Statement.*Operations.*",
        ".*Consolidated.*Statement.*of.*Incom.*",
        ".*Consolidated.*Statement.*Inc.*",
        ".*Consolidated.*Statement.*Earnings.*",
        ".*Income Statement.*",
    ]
    sorted = False
    no_of_years = 3
    year_flag = 0  # assuming years not found initially
    for j in IncomeStatementdict:
        count = 0
        for line in lines:
            count += 1
            if re.search(j, line, re.IGNORECASE):
                print("Found Statement of Income")
                break

        for line in lines[count:]:
            res = re.findall('[0-9]{4}', line)
            if len(res) >= 2:
                year_flag = 1  # years found
                break
        if year_flag:
            break
    if year_flag:
        years = list(map(int, res))  # convert years to numbers
        no_of_years = len(years)
        if no_of_years > 3:  # if years more than 3
            list_years = years[:]
            list_years.sort()
            if list_years == years:  # if years are already sorted & in ascending order
                sorted = True
            if sorted:
                years = years[-3:]  # last 3 years
            else:
                years = years[:3]  # first 3 years

    else:
        years = [2017, 2016, 2015]  # Use default years
        print("Used Default Years=========")
    return years, no_of_years, sorted


def preprocessing(term_list, years, unit_used):
    new_list = []
    if not term_list or term_list is None or term_list == []:
        for i in years:
            new_list.append(0)
        term_list = new_list
    else:
        term_list = term_list[-len(years):]  # take exact no of values as no of years from the right most
        if sorted:
            term_list = term_list[-len(years):]
        else:
            term_list = term_list[:len(years)]
        for ele in term_list:
            ele = ele.replace("(", "-")
            ele = ele.replace(")", "")
            if unit_used.lower() == "millions":
                new_list.append(float(ele))
            else:
                new_list.append(float(ele) / 1000)
        term_list = new_list
    return term_list


def connect_db():
    con = None
    try:
        con = mysql.connector.connect(host="IP",
                                      database='',
                                      user='',
                                      password='')
        db_Info = con.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
    except Exception as e:
        print(e)

    return con


def get_kpi_pl_values(total_revenue, sga, da, cogs, gross_profit, ebitda, gross_margin, ebit_margin, ebitda_margin,
                      ebt_margin, net_income_margin):
    """
    Gets the Income Statement KPI's
    """

    try:
        if all(v != 0 for v in total_revenue):
            try:
                revenue_cagr = (pow(total_revenue[0] / total_revenue[-1], 1 / 2) - 1) * 100
                revenue_cagr = round(revenue_cagr, 1)
            except:
                revenue_cagr = 0
            sga_as_percent_of_revenue = [a / b for a, b in zip(sga, total_revenue)]
            avg_sga_as_percent_of_revenue = (sum(sga_as_percent_of_revenue) / len(sga_as_percent_of_revenue)) * 100
            avg_sga_as_percent_of_revenue = round(avg_sga_as_percent_of_revenue, 1)
            da_as_percent_of_revenue = [a / b for a, b in zip(da, total_revenue)]
            avg_da_as_percent_of_revenue = (sum(da_as_percent_of_revenue) / len(da_as_percent_of_revenue)) * 100
            avg_da_as_percent_of_revenue = round(avg_da_as_percent_of_revenue, 1)
        else:
            revenue_cagr = 0
            avg_sga_as_percent_of_revenue = 0
            avg_da_as_percent_of_revenue = 0

        if all(v != 0 for v in cogs):
            try:
                cogs_cagr = (pow(cogs[0] / cogs[-1], 1 / 2) - 1) * 100
                cogs_cagr = round(cogs_cagr, 1)
            except:
                cogs_cagr = 0
        else:
            cogs_cagr = 0
        if all(v != 0 for v in gross_profit):
            try:
                gross_profit_cagr = (pow(gross_profit[0] / gross_profit[-1], 1 / 2) - 1) * 100
                gross_profit_cagr = round(gross_profit_cagr, 1)
            except:
                gross_profit_cagr = 0
        else:
            gross_profit_cagr = 0
        if all(v != 0 for v in ebitda):
            try:
                ebit_da_cagr = (pow(ebitda[0] / ebitda[-1], 1 / 2) - 1) * 100
                # print(ebit_da_cagr,type(ebit_da_cagr),ebitda)
                ebit_da_cagr = round(ebit_da_cagr, 1)
            except:
                ebit_da_cagr = 0
        else:
            ebit_da_cagr = 0

        avg_ebit_da_margin = sum(ebitda_margin) / len(ebitda_margin)
        avg_ebit_da_margin = round(avg_ebit_da_margin, 1)
        avg_gross_margin = sum(gross_margin) / len(gross_margin)
        avg_gross_margin = round(avg_gross_margin, 1)
        avg_ebit_margin = sum(ebit_margin) / len(ebit_margin)
        avg_ebit_margin = round(avg_ebit_margin, 1)
        avg_ebt_margin = sum(ebt_margin) / len(ebt_margin)
        avg_ebt_margin = round(avg_ebt_margin, 1)
        avg_net_income_margin = sum(net_income_margin) / len(net_income_margin)
        avg_net_income_margin = round(avg_net_income_margin, 1)

    except Exception as e:
        print("Error in PL KPI's", e)
        traceback.print_exc()

    return revenue_cagr, cogs_cagr, gross_profit_cagr, ebit_da_cagr, avg_gross_margin, avg_sga_as_percent_of_revenue, avg_ebit_margin, avg_da_as_percent_of_revenue, avg_ebit_da_margin, avg_ebt_margin, avg_net_income_margin


def get_kpi_bs_values(dso, inventorydays, othercurrentassetspercent, dpo, accruedliabilitiespercent,
                      othercurrentliabilitiespercent):
    """
    gets the balancesheet KPI's
    """
    try:
        avg_days_sales_outstanding_dso = round(sum(dso) / len(dso))

        avg_inventory_days = round(sum(inventorydays) / len(inventorydays))

        avg_other_current_assets_as_percent_of_revenue = round(
            sum(othercurrentassetspercent) / len(othercurrentassetspercent))

        avg_days_sales_outstanding_dpo = round(sum(dpo) / len(dpo))

        avg_accrued_liabilities_as_percent_of_cogs = round(
            sum(accruedliabilitiespercent) / len(accruedliabilitiespercent))

        avg_other_current_liabilities_as_percent_of_cogs = round(
            sum(othercurrentliabilitiespercent) / len(othercurrentliabilitiespercent))

    except Exception as e:
        print("error in BS KPI's", e)
        traceback.print_exc()

    return avg_days_sales_outstanding_dso, avg_inventory_days, avg_other_current_assets_as_percent_of_revenue, avg_days_sales_outstanding_dpo, avg_accrued_liabilities_as_percent_of_cogs, avg_other_current_liabilities_as_percent_of_cogs


class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level


def main_function(file_path, model_name, company_name, period, user, industry, statement_type, filename):
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('/home/srinidhi/angular/ExtractedFiles/' + company_name + '.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # set filter to log only DEBUG lines
    handler.addFilter(MyFilter(logging.DEBUG))
    logger.addHandler(handler)
    current_datetime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    message = "Success"
    try:
        pdftotextlines = ""

        print("=============Program Started============")
        filepath, file1 = os.path.split(file_path)
        pdf_filename = file1.rsplit(".", 1)[0]
        print(pdf_filename)

        txt_file_path = '/home/srinidhi/angular/ExtractedFiles/' + pdf_filename + '.txt'

        term_dict = {}
        total_revenue_patterns = ["Revenues", "Net sales", "Total revenue", "Net revenue", "Net Revenue",
                                  "Net Revenues", "Total net sales", "Revenues", "Total revenues",
                                  "NET OPERATING REVENUES",
                                  "Total Net Revenue", "Total Revenue", "Total Revenues",
                                  "Revenue", "Sales to customer", "Net Sale", "Net Sales", "NET SALES", "Net sales",
                                  "Total net revenues.*", "net sales", "Total sales", "Sales"]
        depriciation_amort = ["Depreciation and amortization",
                              "Depreciation and amortization of property, equipment and intangibles",
                              "Depreciation, amortization, and other",
                              "Depreciation and amortization expense",
                              "Depreciation and amortization expenses",
                              "Depreciation expense",
                              "Depreciation",
                              ]

        url = "/home/srinidhi/angular/ExtractedFiles/" + pdf_filename + ".pdf"
        try:
            fPDFExtractedText = open(txt_file_path, "w")
            pdf = pdfplumber.open(url)
            table_rows = ""
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=1, y_tolerance=1)

                fPDFExtractedText.write("\nPage#" + str(page.page_number))

                fPDFExtractedText.writelines("\n")
                if text is not None:
                    text = text.replace(u'\xA0', ' ')
                    text = text.replace('  ', ' ')
                    text = re.sub('[. .]{3,100}', ' ', text)
                    fPDFExtractedText.writelines(text)
                    pdftotextlines += text
        except Exception as e:
            print("Error In PDF To Text Conversion to Writing to File", e)
        finally:
            fPDFExtractedText.close()  # close the file
        lines = pdftotextlines.split("\n")  # split by lines

        # lines = table_rows.split("\n")

        output_obj = get_prediction(file_path, model_name)

        key_count = len(output_obj.payload)
        # print(output_obj.payload)
        with open('/home/srinidhi/angular/ExtractedFiles/' + pdf_filename + '.json', 'w') as of:
            of.writelines(str(output_obj.payload))

        for i in range(0, key_count):
            display_name = output_obj.payload[i].display_name
            content = output_obj.payload[i].text_extraction.text_segment.content
            values_list = []
            score = output_obj.payload[i].text_extraction.score
            values_list.append(content)
            values_list.append(score)
            if term_dict.get(display_name) == None:
                term_dict[display_name] = values_list
            else:
                existing_term = term_dict.get(display_name)
                if score > existing_term[1]:
                    term_dict[display_name] = values_list

        grouping_dict = {}
        temp_array = []
        for i in range(0, key_count):
            display_name = output_obj.payload[i].display_name
            content = output_obj.payload[i].text_extraction.text_segment.content
            if display_name == "CashEquivalents":
                disp_name = display_name
                temp_array.append(content)
                grouping_dict[disp_name] = temp_array

        temp_array = []
        for i in range(0, key_count):
            display_name = output_obj.payload[i].display_name
            content = output_obj.payload[i].text_extraction.text_segment.content

            if display_name == "PPE":
                disp_name = display_name
                temp_array.append(content)
                grouping_dict[disp_name] = temp_array

        temp_array = []
        for i in range(0, key_count):
            display_name = output_obj.payload[i].display_name
            content = output_obj.payload[i].text_extraction.text_segment.content
            if display_name == "CurrentPortionLongTermDebt":
                disp_name = display_name
                temp_array.append(content)
                grouping_dict[disp_name] = temp_array

        temp_array = []
        for i in range(0, key_count):
            display_name = output_obj.payload[i].display_name
            content = output_obj.payload[i].text_extraction.text_segment.content
            if display_name == "LongTermDebt":
                disp_name = display_name
                temp_array.append(content)
                grouping_dict[disp_name] = temp_array

        print(grouping_dict, "================>Grouping Dict")

        dict_final = {}
        try:
            years, no_of_years, sorted = years_fun(lines)

        except Exception as e:
            print(e, "Exception in Year Fetching")

        sorted_years = years
        sorted_years.sort(reverse=True)

        years_association = {}

        if sorted:
            balance_sheet_years = years[-2:]
        else:
            balance_sheet_years = years[:2]

        latest_val = 0
        for year in sorted_years:
            years_association[year] = latest_val
            latest_val -= 1

        count = 0

        try:
            Company = term_dict["Company"][0]
        except Exception as e:
            Company = 'NA'
            print("Comapny Name not found. Marking it \"NA\"")

        try:
            BalanceSheetStatement = term_dict["BalanceSheetStatement"][0]
        except Exception as e:
            BalanceSheetStatement = 'Consolidated Balance Sheet'
            print("BalanceSheetStatement Name not found. Marking it \"Consolidated Balance Sheet\"")
        try:
            AccountsReceivable_term = term_dict["AccountsReceivable"][0]
        except Exception as e:
            AccountsReceivable_term = 'Accounts receivable'

        try:
            Inventories_term = term_dict["Inventories"][0]
        except Exception as e:
            Inventories_term = 'Inventories'

        try:
            AccountsPayable_term = term_dict["AccountsPayable"][0]
        except Exception as e:
            AccountsPayable_term = 'Accounts payable'

        ## fetch units ###

        try:
            unit = term_dict.get("Units")
            unit_used = unit[0]
        except Exception as e:
            unit_used = "millions"
            print(e)
            print("=======units not found, using default=======")

        for key in term_dict.keys():
            for line in lines:  # loop through all rows

                # line = line.replace("’","") # repalce "\'"
                # line = line.replace("'","") # repalce "\'"
                # line = line.replace("\342\200\231","") # repalce "\'"
                # term = term_dict[key][0].replace("\'","") # repalce "\'"
                # term = term.replace("’","") # repalce "\'"
                line_tmp = re.sub('[\W_]+', '', line)
                term = re.sub('[\W_]+', '', term_dict[key][0])

                if term in line_tmp:
                    # print(term_dict[key][0],"============",line)
                    try:
                        line = line.replace(',', '')
                        line = line.replace('$', '')
                        values = re.findall("\(?[0-9.]{1,10}\)?", line)
                        if len(values) >= 2:
                            dict_final[key] = values
                    except Exception as e:
                        print("exception in fetching", e)
                    break

        # ================Grouping Dict Fetching  values==========================
        grouping_values = {}
        for key, values in grouping_dict.items():
            temp_list = []
            for value in values:
                for line in lines:
                    line_tmp = re.sub('[\W_]+', '', line)
                    value = re.sub('[\W_]+', '', value)
                    if value in line_tmp:
                        line = line.replace(',', '')
                        line = line.replace('$', '')
                        numbers = re.findall("\(?[0-9.]{1,10}\)?", line)
                        if len(numbers) >= 2:
                            temp_list.append(numbers)
                            break
            grouping_values[key] = temp_list

        for key, values in grouping_values.items():
            if len(values) == 0:
                grouping_values[key] = preprocessing(values, balance_sheet_years, unit_used)
            else:
                temp_sum = []
                for i in range(len(values[0])):
                    temp_sum.append(0)
                for value in values:
                    value = preprocessing(value, balance_sheet_years, unit_used)
                    temp_sum = [i + j for i, j in zip(temp_sum, value)]

                grouping_values[key] = temp_sum

        try:
            DandA = term_dict["DandA"][0]
            if re.search("amortization", DandA, re.IGNORECASE) is None:
                amort_flag = 0
            else:
                amort_flag = 1

        except:
            amort_flag = 1

        amort = []
        try:
            if not amort_flag:
                for line in lines:

                    if line.startswith("Amortization"):
                        line = line.replace(',', '')
                        line = line.replace('$', '')
                        amort = re.findall("\(?[0-9.]{1,10}\)?", line)
                        if len(amort) >= 2:
                            break
        except:
            pass
        AccruedLiabilities = []
        AccruedLiabilities_sum = [0, 0]
        try:
            start = 0
            for line in lines:
                start += 1
                if re.search(BalanceSheetStatement, line, re.IGNORECASE):
                    break
            end = 0
            for line in lines:
                end += 1
                if re.search(term_dict["TotalShareholdersEquity"][0], line, re.IGNORECASE):
                    break
            for line in lines[start:end]:
                if re.search("Accrued", line, re.IGNORECASE):
                    line = line.replace(',', '')
                    line = line.replace('$', '')
                    AccruedLiabilities = re.findall("\(?[0-9.]{1,10}\)?", line)
                    if len(AccruedLiabilities) >= 2:
                        AccruedLiabilities = preprocessing(AccruedLiabilities, balance_sheet_years, unit_used)
                        AccruedLiabilities_sum = [i + j for i, j in zip(AccruedLiabilities, AccruedLiabilities_sum)]
        except Exception as e:
            print(e, "Exception in accrued Fetching")

        ## Accounts recievables

        try:
            start = 0
            for line in lines:
                start += 1
                if re.search(BalanceSheetStatement, line, re.IGNORECASE):
                    break
            end = 0
            for line in lines:
                end += 1
                if re.search(term_dict["TotalShareholdersEquity"][0], line, re.IGNORECASE):
                    break
            found_account_receivable = False
            found_inventories = False
            found_account_payables = False
            AccountsReceivable = []
            Inventories = []
            AccountsPayable = []
            for line in lines[start:end]:
                if re.search(AccountsReceivable_term, line, re.IGNORECASE):
                    line = line.replace(',', '')
                    line = line.replace('$', '')
                    AccountsReceivable = re.findall("\(?[0-9.]{1,10}\)?", line)
                    if len(AccountsReceivable) >= 2:
                        found_account_receivable = True
                if re.search(AccountsPayable_term, line, re.IGNORECASE):
                    line = line.replace(',', '')
                    line = line.replace('$', '')
                    AccountsPayable = re.findall("\(?[0-9.]{1,10}\)?", line)
                    if len(AccountsPayable) >= 2:
                        found_account_payables = True

                if re.search(Inventories_term, line, re.IGNORECASE):
                    line = line.replace(',', '')
                    line = line.replace('$', '')
                    Inventories = re.findall("\(?[0-9.]{1,10}\)?", line)
                    if len(Inventories) >= 2:
                        found_inventories = True
                if found_account_payables and found_account_receivable and found_inventories:
                    break


        except Exception as e:
            print(e, "Exception in accounts receivables,payables,inventories")

        AccountsReceivable = preprocessing(AccountsReceivable, balance_sheet_years, unit_used)
        AccountsPayable = preprocessing(AccountsPayable, balance_sheet_years, unit_used)
        Inventories = preprocessing(Inventories, balance_sheet_years, unit_used)

        total_net_found = 0
        for i in total_revenue_patterns:
            for line in lines:  # loop through all rows
                if i in line:
                    line = line.replace(',', '')
                    line = line.replace('$', '')
                    total_net = re.findall("\S[0-9.,]+\S|\S[0-9]+\S", line)
                    dict_final['TotalRevenue'] = total_net
                    if len(total_net) >= 2:
                        total_net_found = 1

                        break
            if total_net_found:
                break

        list_TR = dict_final.get('TotalRevenue')
        TotalRevenue = preprocessing(list_TR, years, unit_used)

        list_COGS = dict_final.get('COGS')
        COGS = preprocessing(list_COGS, years, unit_used)
        COGS = [abs(val) for val in COGS]

        list_GrossProfit = dict_final.get('GrossProfit')
        GrossProfit = preprocessing(list_GrossProfit, years, unit_used)
        if not any(GrossProfit):
            GrossProfit = [i - j for i, j in zip(map(float, TotalRevenue), map(float, COGS))]

        list_EBIT = dict_final.get('EBIT')
        EBIT = preprocessing(list_EBIT, years, unit_used)
        if list_EBIT is not None:
            SGA = [i - j for i, j in zip(map(float, GrossProfit), map(float, EBIT))]

        if list_EBIT is None:
            list_SGA = dict_final.get('SGA')
            SGA = preprocessing(list_SGA, years, unit_used)
            SGA = [abs(val) for val in SGA]
            EBIT = [i - j for i, j in zip(map(float, GrossProfit), map(float, SGA))]

        if list_EBIT is not None:
            SGA = [i - j for i, j in zip(map(float, GrossProfit), map(float, EBIT))]

        list_DandA = dict_final.get('DandA')
        DandA = preprocessing(list_DandA, years, unit_used)
        amort = preprocessing(amort, years, unit_used)

        if len(DandA) == len(amort):
            DandA = [sum(x) for x in zip(DandA, amort)]
        else:
            DandA_updated = []
            for val in DandA:
                val += 0
                DandA_updated.append(val)
            DandA = DandA_updated

        list_EBT = dict_final.get('EBT')
        EBT = preprocessing(list_EBT, years, unit_used)

        if list_EBT is None:
            list_netInterest = dict_final.get('InterestExpense')
            netInterest = preprocessing(list_netInterest, years, unit_used)
            EBT = [i - j for i, j in zip(map(float, EBIT), map(float, netInterest))]
        else:
            netInterest = [i - j for i, j in zip(map(float, EBIT), map(float, EBT))]

        list_netIncome = dict_final.get('NetIncome')
        netIncome = preprocessing(list_netIncome, years, unit_used)

        list_Taxes = dict_final.get('Taxes')
        Taxes = preprocessing(list_Taxes, years, unit_used)

        if list_Taxes is None:
            Taxes = [i - j for i, j in zip(map(float, EBT), map(float, netIncome))]

        if list_netIncome is None:
            netIncome = [i - j for i, j in zip(map(float, EBT), map(float, Taxes))]

        otherIncome = []
        for i in range(len(years)):
            otherIncome.append('0')
        EBT = EBT[:3]

        ############ Balance Sheet Processing Start##########

        # CashEquivalents = dict_final.get('CashEquivalents')
        CashEquivalents = grouping_values.get('CashEquivalents')
        if CashEquivalents is None:
            CashEquivalents = dict_final.get('CashEquivalents')
            CashEquivalents = preprocessing(CashEquivalents, balance_sheet_years, unit_used)
        print(CashEquivalents, "CashEquivalents")

        # AccountsReceivable = dict_final.get('AccountsReceivable')
        # AccountsReceivable=preprocessing(AccountsReceivable,balance_sheet_years,unit_used)
        print(AccountsReceivable, "AccountsReceivable")

        # Inventories = dict_final.get('Inventories')
        # Inventories=preprocessing(Inventories,balance_sheet_years,unit_used)
        print(Inventories, "Inventories")

        TotalCurrentAssets = dict_final.get('TotalCurrentAssets')
        TotalCurrentAssets = preprocessing(TotalCurrentAssets, balance_sheet_years, unit_used)
        print(TotalCurrentAssets, "TotalCurrentAssets")

        # PPE = dict_final.get('PPE')
        PPE = grouping_values.get('PPE')
        if PPE is None:
            PPE = dict_final.get('PPE')
            PPE = preprocessing(PPE, balance_sheet_years, unit_used)
        print(PPE, "PPE")

        Goodwill = dict_final.get('Goodwill')
        Goodwill = preprocessing(Goodwill, balance_sheet_years, unit_used)
        print(Goodwill, "Goodwill")

        IntangibleAssets = dict_final.get('IntangibleAssets')
        IntangibleAssets = preprocessing(IntangibleAssets, balance_sheet_years, unit_used)
        print(IntangibleAssets, "IntangibleAssets")

        TotalAssets = dict_final.get('TotalAssets')
        TotalAssets = preprocessing(TotalAssets, balance_sheet_years, unit_used)
        print(TotalAssets, "TotalAssets")

        # CurrentPortionLongTermDebt = dict_final.get('CurrentPortionLongTermDebt')
        CurrentPortionLongTermDebt = grouping_values.get('CurrentPortionLongTermDebt')
        if CurrentPortionLongTermDebt is None:
            CurrentPortionLongTermDebt = dict_final.get('CurrentPortionLongTermDebt')
            CurrentPortionLongTermDebt = preprocessing(CurrentPortionLongTermDebt, balance_sheet_years, unit_used)
        print(CurrentPortionLongTermDebt, "CurrentPortionLongTermDebt")

        # AccountsPayable = dict_final.get('AccountsPayable')
        # AccountsPayable=preprocessing(AccountsPayable,balance_sheet_years,unit_used)
        print(AccountsPayable, "AccountsPayable")

        # AccruedLiabilities = dict_final.get('AccruedLiabilities')
        # AccruedLiabilities=preprocessing(AccruedLiabilities,balance_sheet_years,unit_used)
        print(AccruedLiabilities_sum, "AccruedLiabilities")

        TotalCurrentLiabilities = dict_final.get('TotalCurrentLiabilities')
        TotalCurrentLiabilities = preprocessing(TotalCurrentLiabilities, balance_sheet_years, unit_used)
        print(TotalCurrentLiabilities, "TotalCurrentLiabilities")

        # LongTermDebt = dict_final.get('LongTermDebt')
        LongTermDebt = grouping_values.get('LongTermDebt')
        if LongTermDebt is None:
            LongTermDebt = dict_final.get('LongTermDebt')
            LongTermDebt = preprocessing(LongTermDebt, balance_sheet_years, unit_used)
        print(LongTermDebt, "LongTermDebt")

        TotalLiabilities = dict_final.get('TotalLiabilities')
        TotalLiabilities = preprocessing(TotalLiabilities, balance_sheet_years, unit_used)
        print(TotalLiabilities, "TotalLiabilities")

        TotalShareholdersEquity = dict_final.get('TotalShareholdersEquity')
        TotalShareholdersEquity = preprocessing(TotalShareholdersEquity, balance_sheet_years, unit_used)
        print(TotalShareholdersEquity, "TotalShareholdersEquity")

        TotalLiabilitiesAndEquity = dict_final.get('TotalLiabilitiesAndEquity')
        TotalLiabilitiesAndEquity = preprocessing(TotalLiabilitiesAndEquity, balance_sheet_years, unit_used)
        print(TotalLiabilitiesAndEquity, "TotalLiabilitiesAndEquity")

        if all(TotalLiability == 0 for TotalLiability in TotalLiabilities):
            TotalLiabilities = [i - j for i, j in zip(TotalLiabilitiesAndEquity, TotalShareholdersEquity)]
            print("Derived TotalLiabilities", TotalLiabilities)

        OtherCurrentLiabilities = []
        OtherCurrentAssets = []
        OtherAssets = []
        OtherLiabilities = []
        for i in range(len(TotalCurrentAssets)):
            temp_val1 = TotalCurrentAssets[i] - (CashEquivalents[i] + AccountsReceivable[i] + Inventories[i])
            OtherCurrentAssets.append(temp_val1)

            temp_val2 = TotalAssets[i] - (PPE[i] + IntangibleAssets[i] + Goodwill[i] + TotalCurrentAssets[i])
            OtherAssets.append(temp_val2)

            temp_val3 = TotalCurrentLiabilities[i] - (
                        CurrentPortionLongTermDebt[i] + AccountsPayable[i] + AccruedLiabilities_sum[i])
            OtherCurrentLiabilities.append(temp_val3)

            temp_val4 = TotalLiabilities[i] - LongTermDebt[i] - TotalCurrentLiabilities[i]
            OtherLiabilities.append(temp_val4)

        print("############ Balance Sheet Processing End ##########")
        ############ Balance Sheet Processing End ##########

        years_in_ascending = years[:]
        years_in_ascending.sort(reverse=True)

        if years != years_in_ascending:
            years = years[::-1]
            EBT = EBT[::-1]
            otherIncome = otherIncome[::-1]
            TotalRevenue = TotalRevenue[::-1]
            COGS = COGS[::-1]
            SGA = SGA[::-1]
            DandA = DandA[::-1]
            netInterest = netInterest[::-1]
            Taxes = Taxes[::-1]
            GrossProfit = GrossProfit[::-1]
            EBIT = EBIT[::-1]
            netIncome = netIncome[::-1]

        print(EBIT, "EBIT")
        print(otherIncome, "otherIncome")
        print(EBT, "EBT")
        print(otherIncome, "otherIncome")
        print(COGS, "COGS")
        print(TotalRevenue, "TotalRevenue")
        print(SGA, "SGA")
        print(Taxes, "Taxes")
        print(years, "years")
        print(netIncome, "netIncome")
        print(GrossProfit, "GrossProfit")
        print(DandA, "DandA")
        created_on = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        connection = connect_db()
        cursor = connection.cursor()

        projections = 4  # hardcodedd
        query = "insert into company_master (companyname,company,period,actuals,projections,createdby,createdon,filename,industry,statementtype)" \
                "values ('" + company_name + "','" + Company + "','" + period + "'," + str(len(years)) + "," + str(
            projections) + ",'" + user + "','" + created_on + "','" + filename + "','" + industry + "','" + statement_type + "')"

        cursor.execute(query)
        connection.commit()
        ebitda_list = []
        grossprofitmargin_list = []
        ebitmargin_list = []
        ebitdamargin_list = []
        ebtmargin_list = []
        netincomemargin_list = []
        pnlyears = []
        for i in range(len(years)):
            latest_value = years_association[years[i]]
            ebitda = EBIT[i] + DandA[i]
            ebitda_list.append(ebitda)
            if all(v == 0 for v in TotalRevenue):
                grossprofitmargin = 0
                ebitmargin = 0
                ebitdamargin = 0
                ebtmargin = 0
                netincomemargin = 0
            else:
                try:
                    grossprofitmargin = float((GrossProfit[i] / TotalRevenue[i]) * 100)
                    grossprofitmargin_list.append(grossprofitmargin)
                    ebitmargin = float((EBIT[i] / TotalRevenue[i]) * 100)
                    ebitmargin_list.append(ebitmargin)
                    ebitdamargin = float((ebitda / TotalRevenue[i]) * 100)
                    ebitdamargin_list.append(ebitdamargin)
                    ebtmargin = float((EBT[i] / TotalRevenue[i]) * 100)
                    ebtmargin_list.append(ebtmargin)
                    netincomemargin = float((netIncome[i] / TotalRevenue[i]) * 100)
                    netincomemargin_list.append(netincomemargin)
                except Exception as e:
                    print("exception margin values")
            if len(years) - 1 != i:
                try:
                    revenuepercent = ((TotalRevenue[i] - TotalRevenue[i + 1]) / TotalRevenue[i + 1]) * 100
                    cogspercent = (COGS[i] / TotalRevenue[i]) * 100
                    sgapercent = (SGA[i] / TotalRevenue[i]) * 100
                    dapercent = (DandA[i] / TotalRevenue[i]) * 100

                except:
                    revenuepercent = 0
                    cogspercent = 0
                    sgapercent = 0
                    dapercent = 0
                    print("excpetion in Total Revenue Percenetage")
            else:
                revenuepercent = 0
                cogspercent = 0
                sgapercent = 0
                dapercent = 0

            pnlyears = years
            query = "insert into company_actuals (companyname,asof,latest,totalrevenue,cogs,sga,da,netinterest,otherincome," \
                    "taxes,grossprofit,ebit,ebitda,netincome,grossprofitmargin,ebitmargin,ebitdamargin,ebtmargin,netincomemargin,ebt,revenuepercent,cogspercent,sgapercent,dapercent) values(" \
                    "'" + company_name + "'," + str(years[i]) + "," + str(
                latest_value) + "," + str(TotalRevenue[i]) + "," + str(COGS[i]) + "," + str(SGA[i]) + "," + str(
                DandA[i]) + "," + str(netInterest[i]) + "," + str(otherIncome[i]) + "," + str(
                abs(Taxes[i])) + "," + str(
                GrossProfit[i]) + "," + str(EBIT[i]) + "," + str(ebitda) + "," + str(netIncome[i]) + "," + str(
                grossprofitmargin) + "," + str(ebitmargin) + "," + str(ebitdamargin) + "," + str(
                ebtmargin) + "," + str(netincomemargin) + "," + str(EBT[i]) + "," + str(revenuepercent) + "," + str(
                cogspercent) + "," + str(sgapercent) + "," + str(dapercent) + ")"
            cursor.execute(query)
        connection.commit()  # save records

        ### Balance Sheet Insertion ===================
        years = balance_sheet_years[:]
        years.sort(reverse=True)

        if balance_sheet_years != years:
            years = balance_sheet_years[::-1]
            AccountsReceivable = AccountsReceivable[::-1]
            CashEquivalents = CashEquivalents[::-1]
            Inventories = Inventories[::-1]
            TotalCurrentAssets = TotalCurrentAssets[::-1]
            PPE = PPE[::-1]
            Goodwill = Goodwill[::-1]
            IntangibleAssets = IntangibleAssets[::-1]
            TotalAssets = TotalAssets[::-1]
            CurrentPortionLongTermDebt = CurrentPortionLongTermDebt[::-1]
            AccountsPayable = AccountsPayable[::-1]
            AccruedLiabilities_sum = AccruedLiabilities_sum[::-1]
            TotalCurrentLiabilities = TotalCurrentLiabilities[::-1]
            LongTermDebt = LongTermDebt[::-1]
            TotalLiabilities = TotalLiabilities[::-1]
            TotalShareholdersEquity = TotalShareholdersEquity[::-1]
            TotalLiabilitiesAndEquity = TotalLiabilitiesAndEquity[::-1]
            OtherAssets = OtherAssets[::-1]
            OtherCurrentAssets = OtherCurrentAssets[::-1]
            OtherCurrentLiabilities = OtherCurrentLiabilities[::-1]
            OtherLiabilities = OtherLiabilities[::-1]

            ######Calculative Fields Balance Sheet
        print("===========balance Sheet Calculation Start===============")
        if all(v != 0 for v in TotalRevenue):
            dso = [round((a / b) * 365, 2) for a, b in zip(AccountsReceivable, TotalRevenue)]  # round off 2 fractions
            othercurrentassetspercent = [round((a / b) * 100, 2) for a, b in
                                         zip(OtherCurrentAssets, TotalRevenue)]  # round off 2 fractions
        else:
            dso = [i for i in othercurrentassetspercent]
            othercurrentassetspercent = [i for i in othercurrentassetspercent]
        if all(v != 0 for v in COGS):
            dpo = [round((a / b) * 365, 2) for a, b in zip(AccountsPayable, COGS)]  # round off 2 fractions
            inventorydays = [round((a / b) * 365, 2) for a, b in zip(Inventories, COGS)]  # round off 2 fractions
            accruedliabilitiespercent = [round((a / b) * 100, 2) for a, b in
                                         zip(AccruedLiabilities_sum, COGS)]  # round off 2 fractions
            othercurrentliabilitiespercent = [round((a / b) * 100, 2) for a, b in
                                              zip(OtherCurrentLiabilities, COGS)]  # round off 2 fractions
        else:
            dpo = [i for i in COGS]
            inventorydays = [i for i in COGS]
            accruedliabilitiespercent = [i for i in COGS]
            othercurrentliabilitiespercent = [i for i in COGS]
        memocheck = []
        for i, j in zip(TotalAssets, TotalLiabilitiesAndEquity):
            if i == j:
                memocheck.append(0)
            else:
                memocheck.append(1)

        print("===========balance Sheet Calculation End===============")

        # Start Writing to Database

        for i in range(len(years)):
            latest_value = years_association[years[i]]
            query = "insert into balancesheet_actuals(companyname,asof,latest,cashequivalents,accountsreceivable,inventories,othercurrentassets,totalcurrentassets,ppe,intangibleassets,goodwill,otherassets,totalassets,currentportionlongtermdebt,accountspayable,accruedliabilities,othercurrentliabilities,totalcurrentliabilities,longtermdebt,otherliabilities,totalliabilities,totalshareholdersequity,totalliabilitiesandequity,memocheck,totalrevenue,cogs,dso,inventorydays,othercurrentassetspercent,dpo,accruedliabilitiespercent,othercurrentliabilitiespercent) values(" \
                    "'" + company_name + "'," + str(years[i]) + "," + str(
                latest_value) + "," + str(CashEquivalents[i]) + "," + str(AccountsReceivable[i]) + "," + str(
                Inventories[i]) + "," + str(OtherCurrentAssets[i]) + "," + str(
                TotalCurrentAssets[i]) + "," + str(PPE[i]) + "," + str(IntangibleAssets[i]) + "," + str(
                Goodwill[i]) + "," + str(
                OtherAssets[i]) + "," + str(TotalAssets[i]) + "," + str(CurrentPortionLongTermDebt[i]) + "," + str(
                AccountsPayable[i]) + "," + str(AccruedLiabilities_sum[i]) + "," + str(
                OtherCurrentLiabilities[i]) + "," + str(TotalCurrentLiabilities[i]) + "," + str(
                LongTermDebt[i]) + "," + str(
                OtherLiabilities[i]) + "," + str(TotalLiabilities[i]) + "," + str(
                TotalShareholdersEquity[i]) + "," + str(TotalLiabilitiesAndEquity[i]) + "," + str(
                memocheck[i]) + "," + str(TotalRevenue[i]) + "," + str(COGS[i]) + "," + str(dso[i]) + "," + str(
                inventorydays[i]) + "," + str(othercurrentassetspercent[i]) + "," + str(dpo[i]) + "," + str(
                accruedliabilitiespercent[i]) + "," + str(othercurrentliabilitiespercent[i]) + ")"
            cursor.execute(query)
        connection.commit()

        ############# KPI P&L Actuals start ##################

        kpi_pl = get_kpi_pl_values(TotalRevenue, SGA, DandA, COGS, GrossProfit, ebitda_list, grossprofitmargin_list,
                                   ebitmargin_list, ebitdamargin_list, ebtmargin_list, netincomemargin_list)

        query = "insert into kpi_pnl_actuals(companyname,fromyear,toyear,revenuecagr,cogscagr,grossprofitcagr,ebitdacagr,avggrossmargin,avgsgaasrevenue,avgebitmargin,avgdnaasrevenue,avgebitdamargin,avgebtmargin,avgnetincomemargin) values(" \
                "'" + company_name + "'," + str(pnlyears[-1]) + "," + str(
            pnlyears[0]) + "," + str(kpi_pl[0]) + "," + str(kpi_pl[1]) + "," + str(kpi_pl[2]) + "," + str(
            kpi_pl[3]) + "," + str(
            kpi_pl[4]) + "," + str(kpi_pl[5]) + "," + str(kpi_pl[6]) + "," + str(kpi_pl[7]) + "," + str(
            kpi_pl[8]) + "," + str(kpi_pl[9]) + "," + str(kpi_pl[10]) + ")"
        cursor.execute(query)
        connection.commit()
        ############# KPI P&L Actuals end ##################

        ############# KPI BS Actuals start ##################

        kpi_bs = get_kpi_bs_values(dso, inventorydays, othercurrentassetspercent, dpo, accruedliabilitiespercent,
                                   othercurrentliabilitiespercent)
        query = "insert into kpi_bs_actuals(companyname,fromyear,toyear,dso,inventorydays,othercurrentassetspercent,dpo,accruedliabilitiespercent,othercurrentliabilitiespercent) values(" \
                "'" + company_name + "'," + str(years[1]) + "," + str(
            years[0]) + "," + str(kpi_bs[0]) + "," + str(kpi_bs[1]) + "," + str(kpi_bs[2]) + "," + str(
            kpi_bs[3]) + "," + str(
            kpi_bs[4]) + "," + str(kpi_bs[5]) + ")"
        cursor.execute(query)
        connection.commit()

        ########### KPI BS Actuals end############

    except Exception as e:
        print("Error in Program execution", e)
        message = "Extraction Failed"
        traceback.print_exc()
    return message


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    print("File {} uploaded to {}.".format(source_file_name, destination_blob_name))
    return "File {} uploaded to {}.".format(source_file_name, destination_blob_name)


if __name__ == "__main__":
    company_name = sys.argv[1]

    file_path = '/home/srinidhi/angular/ExtractedFiles/' + company_name + ".pdf"
    destination_path = company_name + '/' + company_name + ".pdf"
    upload_blob('sample_pdf', file_path, destination_path)

    file_path = 'gs://sample_pdf/' + company_name + '/' + company_name + '.pdf'
    model_name = 'projects/410058770032/locations/us-central1/models/TEN8689222691011428352'
    period = "Y"
    user = ''
    industry = 'communications'
    statement_type = 'all statements'
    filename = company_name + ".pdf"

    result = main_function(file_path, model_name, company_name, period, user, industry, statement_type, filename)

    print(result)

