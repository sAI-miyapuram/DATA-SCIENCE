def findDecision(obj): #obj[0]: age, obj[1]: sex, obj[2]: cp, obj[3]: trestbps, obj[4]: chol, obj[5]: fbs, obj[6]: restecg, obj[7]: thalach, obj[8]: exang, obj[9]: oldpeak, obj[10]: slope, obj[11]: ca, obj[12]: thal
	# {"feature": "cp", "instances": 303, "metric_value": 0.0718, "depth": 1}
	if obj[2]>0:
		# {"feature": "sex", "instances": 160, "metric_value": 0.0343, "depth": 2}
		if obj[1]>0:
			# {"feature": "slope", "instances": 103, "metric_value": 0.0364, "depth": 3}
			if obj[10]>1:
				# {"feature": "age", "instances": 58, "metric_value": 0.0391, "depth": 4}
				if obj[0]>41.19484335037579:
					# {"feature": "fbs", "instances": 48, "metric_value": 0.048, "depth": 5}
					if obj[5]<=0:
						# {"feature": "trestbps", "instances": 39, "metric_value": 0.0498, "depth": 6}
						if obj[3]<=156:
							# {"feature": "thalach", "instances": 37, "metric_value": 0.0413, "depth": 7}
							if obj[7]<=176.63754418894655:
								# {"feature": "ca", "instances": 31, "metric_value": 0.0528, "depth": 8}
								if obj[11]<=1:
									# {"feature": "oldpeak", "instances": 27, "metric_value": 0.0684, "depth": 9}
									if obj[9]<=0.3:
										# {"feature": "chol", "instances": 19, "metric_value": 0.11, "depth": 10}
										if obj[4]>227:
											# {"feature": "restecg", "instances": 12, "metric_value": 0.0043, "depth": 11}
											if obj[6]>0:
												# {"feature": "thal", "instances": 8, "metric_value": 0.0012, "depth": 12}
												if obj[12]<=2:
													# {"feature": "exang", "instances": 5, "metric_value": 0.0, "depth": 13}
													if obj[8]<=0:
														return 1
													else: return 0.6
												elif obj[12]>2:
													return 0.6666666666666666
												else: return 0.6666666666666666
											elif obj[6]<=0:
												return 0.75
											else: return 0.75
										elif obj[4]<=227:
											return 1
										else: return 1.0
									elif obj[9]>0.3:
										return 1
									else: return 1.0
								elif obj[11]>1:
									return 0.25
								else: return 0.25
							elif obj[7]>176.63754418894655:
								return 1
							else: return 1.0
						elif obj[3]>156:
							return 0
						else: return 0.0
					elif obj[5]>0:
						return 1
					else: return 1.0
				elif obj[0]<=41.19484335037579:
					return 1
				else: return 1.0
			elif obj[10]<=1:
				# {"feature": "ca", "instances": 45, "metric_value": 0.0396, "depth": 4}
				if obj[11]<=0:
					# {"feature": "age", "instances": 29, "metric_value": 0.0502, "depth": 5}
					if obj[0]<=64:
						# {"feature": "fbs", "instances": 27, "metric_value": 0.0789, "depth": 6}
						if obj[5]<=0:
							# {"feature": "chol", "instances": 21, "metric_value": 0.1017, "depth": 7}
							if obj[4]<=270:
								# {"feature": "oldpeak", "instances": 18, "metric_value": 0.1436, "depth": 8}
								if obj[9]>0.6:
									# {"feature": "restecg", "instances": 11, "metric_value": 0.059, "depth": 9}
									if obj[6]>0:
										# {"feature": "thal", "instances": 6, "metric_value": 0.2357, "depth": 10}
										if obj[12]<=2:
											return 0.6666666666666666
										elif obj[12]>2:
											return 0
										else: return 0.0
									elif obj[6]<=0:
										# {"feature": "trestbps", "instances": 5, "metric_value": 0.2, "depth": 10}
										if obj[3]<=130:
											return 1
										elif obj[3]>130:
											return 0.5
										else: return 0.5
									else: return 0.8
								elif obj[9]<=0.6:
									return 1
								else: return 1.0
							elif obj[4]>270:
								return 0
							else: return 0.0
						elif obj[5]>0:
							return 1
						else: return 1.0
					elif obj[0]>64:
						return 0
					else: return 0.0
				elif obj[11]>0:
					# {"feature": "oldpeak", "instances": 16, "metric_value": 0.1268, "depth": 5}
					if obj[9]<=1.8:
						# {"feature": "chol", "instances": 10, "metric_value": 0.0899, "depth": 6}
						if obj[4]<=273:
							# {"feature": "exang", "instances": 8, "metric_value": 0.1464, "depth": 7}
							if obj[8]<=0:
								# {"feature": "age", "instances": 6, "metric_value": 0.2357, "depth": 8}
								if obj[0]<=57:
									return 0.3333333333333333
								elif obj[0]>57:
									return 1
								else: return 1.0
							elif obj[8]>0:
								return 0
							else: return 0.0
						elif obj[4]>273:
							return 0
						else: return 0.0
					elif obj[9]>1.8:
						return 0
					else: return 0.0
				else: return 0.25
			else: return 0.5111111111111111
		elif obj[1]<=0:
			# {"feature": "ca", "instances": 57, "metric_value": 0.1096, "depth": 3}
			if obj[11]<=0:
				return 1
			elif obj[11]>0:
				# {"feature": "age", "instances": 17, "metric_value": 0.1317, "depth": 4}
				if obj[0]<=62:
					# {"feature": "trestbps", "instances": 9, "metric_value": 0.1381, "depth": 5}
					if obj[3]>118:
						# {"feature": "slope", "instances": 6, "metric_value": 0.2113, "depth": 6}
						if obj[10]>1:
							return 0.75
						elif obj[10]<=1:
							return 0
						else: return 0.0
					elif obj[3]<=118:
						return 1
					else: return 1.0
				elif obj[0]>62:
					return 1
				else: return 1.0
			else: return 0.8235294117647058
		else: return 0.9473684210526315
	elif obj[2]<=0:
		# {"feature": "ca", "instances": 143, "metric_value": 0.0847, "depth": 2}
		if obj[11]>0:
			# {"feature": "trestbps", "instances": 78, "metric_value": 0.0636, "depth": 3}
			if obj[3]<=131.87179487179486:
				# {"feature": "sex", "instances": 45, "metric_value": 0.0661, "depth": 4}
				if obj[1]>0:
					# {"feature": "oldpeak", "instances": 40, "metric_value": 0.1007, "depth": 5}
					if obj[9]>0.2:
						return 0
					elif obj[9]<=0.2:
						# {"feature": "thalach", "instances": 13, "metric_value": 0.207, "depth": 6}
						if obj[7]>147:
							return 0
						elif obj[7]<=147:
							return 0.5
						else: return 0.5
					else: return 0.15384615384615385
				elif obj[1]<=0:
					# {"feature": "exang", "instances": 5, "metric_value": 0.4899, "depth": 5}
					if obj[8]<=0:
						return 1
					elif obj[8]>0:
						return 0
					else: return 0.0
				else: return 0.6
			elif obj[3]>131.87179487179486:
				return 0
			else: return 0.0
		elif obj[11]<=0:
			# {"feature": "thal", "instances": 65, "metric_value": 0.0896, "depth": 3}
			if obj[12]<=2:
				# {"feature": "trestbps", "instances": 38, "metric_value": 0.0721, "depth": 4}
				if obj[3]>115:
					# {"feature": "thalach", "instances": 29, "metric_value": 0.0849, "depth": 5}
					if obj[7]>129.73482338536877:
						# {"feature": "exang", "instances": 26, "metric_value": 0.0801, "depth": 6}
						if obj[8]<=0:
							# {"feature": "chol", "instances": 16, "metric_value": 0.1796, "depth": 7}
							if obj[4]<=302:
								return 1
							elif obj[4]>302:
								return 0.5
							else: return 0.5
						elif obj[8]>0:
							# {"feature": "chol", "instances": 10, "metric_value": 0.1838, "depth": 7}
							if obj[4]>204:
								# {"feature": "age", "instances": 7, "metric_value": 0.2497, "depth": 8}
								if obj[0]<=57:
									return 1
								elif obj[0]>57:
									return 0.3333333333333333
								else: return 0.3333333333333333
							elif obj[4]<=204:
								return 0
							else: return 0.0
						else: return 0.5
					elif obj[7]<=129.73482338536877:
						return 0
					else: return 0.0
				elif obj[3]<=115:
					return 1
				else: return 1.0
			elif obj[12]>2:
				# {"feature": "oldpeak", "instances": 27, "metric_value": 0.2033, "depth": 4}
				if obj[9]>0.5:
					return 0
				elif obj[9]<=0.5:
					# {"feature": "age", "instances": 10, "metric_value": 0.1838, "depth": 5}
					if obj[0]>41:
						# {"feature": "chol", "instances": 7, "metric_value": 0.4518, "depth": 6}
						if obj[4]<=234:
							return 1
						elif obj[4]>234:
							return 0
						else: return 0.0
					elif obj[0]<=41:
						return 0
					else: return 0.0
				else: return 0.5
			else: return 0.18518518518518517
		else: return 0.5230769230769231
	else: return 0.2727272727272727
